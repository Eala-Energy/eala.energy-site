---
title: "Twelve zones, and where the surplus goes"
description: "NESO wants to buy reserve in twelve zones. The national saving is small; behind a Scottish constraint, the bigger question is where surplus power goes."
date: 2026-11-27
updated: 2026-11-27
slug: twelve-zones-and-where-the-surplus-goes
tags: [flexibility, curtailment, scotland, ai-compute]
linkedin_url: https://www.linkedin.com/posts/energystorage-bess-neso-share-7532035837669056512-x2OK/
image: /blog/img/twelve-zones-and-where-the-surplus-goes.jpg
image_alt: "Fenced containerised modules on a gravel pad on a Scottish hillside at dusk, one with lit server racks and venting steam, wind turbines on the ridge and a transmission line running down a glen under a rain squall"
image_caption: Illustration
---

Callum forwarded NESO’s paper on twelve balancing zones with one line: “So a battery’s postcode now sets its price. Good news if your sites are in the right places?” [[1]](https://www.neso.energy/document/382216/download)

Possibly, though the financial implications are rather more modest than the headlines suggest.

NESO currently buys reserve and response nationally. Under its proposal, Britain would be divided into twelve zones, three of them in Scotland, with the same service potentially attracting different prices in the same half-hour whenever a network constraint limits delivery between zones [[1]](https://www.neso.energy/document/382216/download) [[2]](https://www.ess-news.com/2026/11/24/uk-grid-operator-plans-locational-procurement-for-ancillary-services/). The modelling commissioned by NESO puts the annual net saving at around £7m [[3]](https://www.n-side.com/en/insights/defining-locational-procurement-for-neso-in-great-britain/) [[4]](https://www.neso.energy/document/373051/download), against a constraint bill of well over £1bn a year [[5]](https://nao.org.uk/press-releases/delays-to-electricity-grid-upgrades-risk-higher-bills/).

“Small money, then.”

Nationally, yes. For an individual asset, the difference could be quite material. A modest aggregate saving can conceal substantial differences in prices between locations.

What interests me more is the reasoning behind the proposal. NESO describes reserve that cannot be delivered across a constrained boundary as “sterilised” [[1]](https://www.neso.energy/document/382216/download). Consider upward reserve held in northern Scotland. There is little value in having another megawatt available if the transmission lines heading south are already at capacity.

What might be considerably more valuable in that location is somewhere to put the surplus power.

“That’s your compute argument again.”

It is, although there was an interesting development this week. Statera secured £112m of debt for its 290 MW Exeter battery, four months after launch. It is a two-hour battery with a five-year agreement under which Statkraft provides market access while Statera’s own team determines the trading strategy [[6]](https://www.solarpowerportal.co.uk/energy-storage/statera-energy-financial-close-290mw-580mwh-bess-east-devon). The owner has kept the commercial decisions in-house and outsourced the market infrastructure.

At a location where wind generation is regularly curtailed, those decisions become even more interesting. A few megawatts of containerised compute alongside a battery with six to eight hours of storage would allow the operator to decide, hour by hour, how best to use the available electricity. Some could go towards running AI workloads, some into storage, with the battery also available to provide grid services when economically attractive.

NESO’s proposal that no individual unit should span two zones also has implications for distributed fleets [[1]](https://www.neso.energy/document/382216/download). Each location would need to be optimised against its own network conditions and commercial opportunities.

“And if the difference in zonal prices turns out to be negligible?”

Then reserve revenues remain supplementary, and the economics of the site depend primarily on the compute business, assuming there is a paying customer for it.

We have had years of curtailment data pointing to the geographical imbalance. It would be useful to see how much of that imbalance is reflected in the price of reserve itself.

## Sources

1. NESO, “Locational Procurement: Proposed Market Design for Response and Reserve”, November 2026: the network divided into 12 zones aligned with key transmission boundaries, Scotland into three; sterilised capacity defined as procured capacity that cannot be used effectively in real time because network constraints prevent its delivery; assets in the same registered unit may not span more than one zone. <https://www.neso.energy/document/382216/download>
2. ESS News, “UK grid operator plans locational procurement for ancillary services”, 24 November 2026: the same service could clear at different prices in different zones during constrained periods; consultation open until 8 January 2027. <https://www.ess-news.com/2026/11/24/uk-grid-operator-plans-locational-procurement-for-ancillary-services/>
3. N-SIDE, “Defining Locational Procurement for NESO in Great Britain”, 3 June 2026: quantitative evaluation for NESO; net benefit of the 12-zone model £7.1m over the modelled period, 11.4% of current auction procurement costs. <https://www.n-side.com/en/insights/defining-locational-procurement-for-neso-in-great-britain/>
4. NESO, “Response and Reserve Webinar”, November 2025: 12-zone net benefit of £7.3m per year on April 2024 – June 2025 data. <https://www.neso.energy/document/373051/download>
5. National Audit Office, “Delays to electricity grid upgrades risk higher bills”, September 2026: constraint costs totalled £1.9bn in 2025-26 and could rise to as much as £7.8bn by 2030. <https://nao.org.uk/press-releases/delays-to-electricity-grid-upgrades-risk-higher-bills/>
6. Solar Power Portal, “Statera Energy reaches financial close on 290MW Exeter Storage”, November 2026: £112m of debt for the 290 MW / 580 MWh project; five-year route-to-market agreement with Statkraft, with Statera’s in-house trading team directing strategy; from launch in August to financial close in four months. <https://www.solarpowerportal.co.uk/energy-storage/statera-energy-financial-close-290mw-580mwh-bess-east-devon>
