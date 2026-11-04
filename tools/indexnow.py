#!/usr/bin/env python3
"""Tell IndexNow (Bing, Yandex and others) which eala.energy URLs changed. Standard library only.

    python3 tools/indexnow.py                URLs changed in sitemap.xml by the last merge/commit
    python3 tools/indexnow.py --all          every URL in sitemap.xml
    python3 tools/indexnow.py --dry-run      print the URLs, send nothing
    python3 tools/indexnow.py --base <rev>   compare sitemap.xml with <rev> instead of HEAD^1
    python3 tools/indexnow.py --no-wait      do not wait for the deploy

By default it first waits until the live sitemap matches this commit, because search engines fetch
the URLs as soon as they are told about them. Google does not take part in IndexNow.
The key file in the site root (<key>.txt) proves ownership. It is public by design, not a secret.
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = 'eala.energy'
SITE = f'https://{HOST}'
ENDPOINT = 'https://api.indexnow.org/indexnow'
WAIT_SECONDS = 600
POLL_SECONDS = 20
NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'


def find_key():
    keys = [p.stem for p in ROOT.glob('*.txt') if re.fullmatch(r'[0-9a-f]{32}', p.stem)]
    if len(keys) != 1:
        sys.exit(f'expected exactly one <32 hex>.txt key file in the site root, found {len(keys)}')
    if (ROOT / f'{keys[0]}.txt').read_text().strip() != keys[0]:
        sys.exit('the key file must contain its own name')
    return keys[0]


def sitemap_at(rev):
    """Return {url: lastmod} for sitemap.xml at a git revision; empty if it does not exist there."""
    run = subprocess.run(['git', 'show', f'{rev}:sitemap.xml'], cwd=ROOT, capture_output=True)
    if run.returncode != 0:
        return {}
    return parse_sitemap(run.stdout)


def parse_sitemap(data):
    urls = {}
    for node in ET.fromstring(data).iter(f'{NS}url'):
        urls[node.findtext(f'{NS}loc').strip()] = (node.findtext(f'{NS}lastmod') or '').strip()
    return urls


def changed_urls(old, new):
    """New or updated URLs, plus removed ones: IndexNow also takes URLs that now return 404."""
    changed = [url for url, mod in new.items() if old.get(url) != mod]
    return changed + [url for url in old if url not in new]


def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'eala-energy-indexnow'})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def wait_for_deploy(key, expected):
    deadline = time.monotonic() + WAIT_SECONDS
    while True:
        try:
            if fetch(f'{SITE}/{key}.txt').decode().strip() == key and fetch(f'{SITE}/sitemap.xml') == expected:
                return
        except (urllib.error.URLError, OSError):
            pass
        if time.monotonic() >= deadline:
            sys.exit(f'the live site did not match this commit within {WAIT_SECONDS} s; nothing was sent')
        print('waiting for the deploy...', flush=True)
        time.sleep(POLL_SECONDS)


def submit(key, urls):
    body = json.dumps({'host': HOST, 'key': key, 'keyLocation': f'{SITE}/{key}.txt', 'urlList': urls}).encode()
    request = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                     headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


def main():
    parser = argparse.ArgumentParser(description='Submit changed eala.energy URLs to IndexNow.')
    parser.add_argument('--all', action='store_true', help='submit every URL in sitemap.xml')
    parser.add_argument('--base', default='HEAD^1', help='git revision to compare sitemap.xml with')
    parser.add_argument('--dry-run', action='store_true', help='print the URLs and send nothing')
    parser.add_argument('--no-wait', action='store_true', help='do not wait for the deploy')
    args = parser.parse_args()

    key = find_key()
    local = (ROOT / 'sitemap.xml').read_bytes()
    current = parse_sitemap(local)
    urls = list(current) if args.all else changed_urls(sitemap_at(args.base), current)
    if not urls:
        print('sitemap.xml has no changed URLs; nothing to send')
        return
    print('\n'.join(urls))
    if args.dry_run:
        return
    if not args.no_wait:
        wait_for_deploy(key, local)
    status = submit(key, urls)
    # 200 = received, 202 = received while the key is still being validated.
    if status not in (200, 202):
        sys.exit(f'IndexNow answered HTTP {status}')
    print(f'sent {len(urls)} URL(s), IndexNow answered HTTP {status}')


if __name__ == '__main__':
    main()
