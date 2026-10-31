# Blog ("Insights") — instructions for agents

The site is plain static HTML served by GitHub Pages straight from `main` (no Jekyll: `.nojekyll`).
Posts are Markdown files in `blog/posts/`. `tools/build_blog.py` (Python 3.9+, standard library only)
turns them into static HTML that is committed with the post. There is no server-side build.

## Add a post

```bash
git switch main && git pull && git switch -c post/<slug>
python3 tools/build_blog.py --new "Post title"   # creates blog/posts/<slug>.md with today's dates
# write the post (front matter + body), then:
python3 tools/build_blog.py                      # generates pages, feed, sitemap, llms.txt, nav links
python3 tools/build_blog.py --check              # must print "ok"
```

Copying `blog/posts/_template.md` to `blog/posts/<slug>.md` works too. The template lists every
field and every supported Markdown feature.

## Front matter

```yaml
---
title: "Title as it should appear in search results"
description: "One sentence, at most 155 characters."
date: 2026-11-02          # first publication, YYYY-MM-DD
updated: 2026-11-02       # last substantive edit, YYYY-MM-DD, never earlier than date
slug: title-in-latin-letters
tags: [curtailment, ai-compute]
linkedin_url: https://www.linkedin.com/posts/...   # optional
image: /blog/img/title.png                         # optional, defaults to /preview.png
---
```

The build stops with an error (and writes nothing) if any rule below is broken.

| Field | Rule |
|---|---|
| `title` | required |
| `description` | required, at most 155 characters (meta description, /blog/ list, RSS) |
| `date`, `updated` | required, `YYYY-MM-DD`, `updated` ≥ `date` |
| `slug` | required, lowercase latin letters, digits and single hyphens; unique; becomes `/blog/<slug>/` |
| `tags` | required list, may be empty: `[]` |
| `linkedin_url` | optional, `https://www.linkedin.com/...`; adds "Discussion on LinkedIn" under the post |
| `image` | optional, `https://...` or a site path starting with `/` |

Unknown fields and the string `TODO` anywhere in a post are errors, so unfinished posts cannot ship.

## Writing rules

- **Sources:** cite every number and claim as a Markdown link to the source.
- **Updates:** when you change the substance of a published post, set `updated` to today and rebuild.
  Typo fixes do not need it. Never change `slug` after publication: the old URL would 404.
- **Headings:** the title is the page's only H1. Start sections with `##`; a `#` is turned into `##`.
- **Positioning:** lead with "distributed AI compute infrastructure". Do not lead with battery,
  BESS or storage; that part is the "energy-resilience layer". No financial jargon (IRR, arbitrage,
  LP, returns). Tone: neutral and institutional.
- **Figures:** use only numbers already on the site (3–10 MW, 6–8 hr) or numbers with a cited
  source. Do not invent company metrics.
- **Drafts:** a file whose name starts with `_` is never built. But the repository is public and
  GitHub Pages serves every file in `main`, so never commit anything confidential, drafts included.

### Supported Markdown

Paragraphs, `##`–`######` headings, **bold**, *italic*, `code`, links `[text](url)`, autolinks
`<https://...>`, images `![alt](/path.png)`, one-level `-` and `1.` lists, `>` quotes, fenced code
blocks, `---` rules and simple pipe tables. Not supported: raw HTML (shown as text), nested lists,
footnotes, URLs that contain parentheses. Put images in `blog/img/` and always write alt text.

## Preview locally

```bash
python3 tools/build_blog.py && python3 -m http.server 8000
# open http://localhost:8000/blog/
```

## What the build changes

- `blog/index.html`, `blog/<slug>/index.html`, `blog/feed.xml`: generated, do not edit by hand.
  To change their layout, edit `tools/build_blog.py`.
- `index.html`: the "Insights" link in the menu and footer, between the `<!-- blog:nav -->` and
  `<!-- blog:footer -->` markers. Keep the markers.
- `sitemap.xml`: `/blog/` and every post, `lastmod` = `updated`.
- `llms.txt`: the `## Insights` section.

With no publishable posts, all of the above are removed, so an empty blog is never live.
Deleting a post's `.md` file and rebuilding removes its page.

## Publishing

Publishing happens **only through a pull request into `main`**. Merging the PR deploys the site
within a couple of minutes. Never push to `main` directly. Before opening the PR:

1. `python3 tools/build_blog.py --check` prints `ok`.
2. The post looks right at http://localhost:8000/blog/<slug>/, at desktop width and at 390px.
3. Commit the `.md` file **and** all generated files together.
