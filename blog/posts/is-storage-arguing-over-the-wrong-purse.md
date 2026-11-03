---
title: "Is storage arguing over the wrong purse?"
description: "Battery developers warn Ofgem’s 7.6 GW long-duration round could cut two-hour revenues by 13%. Constraint payments, a bigger bill, ran at £1.9bn."
date: 2026-11-03
updated: 2026-11-03
slug: is-storage-arguing-over-the-wrong-purse
tags: [energy-storage, ldes, curtailment, scotland]
linkedin_url: https://www.linkedin.com/feed/update/urn:li:activity:7523366721555038209
image: /blog/img/is-storage-arguing-over-the-wrong-purse.jpg
image_alt: "Four grey containerised modules on a gravel pad beside a fenced track, on russet moorland at dusk, with one lit from inside and a loch, buildings and a wind turbine tower behind"
---

Priya messaged on Monday, as Hams Hall went live.

“Europe’s largest battery by energy switches on, and the same week eight battery developers publish modelling saying the regulator is backing too much long-duration storage. Which is it?”

Both, oddly.

The first phase at Hams Hall, 350 MW and 1,243 MWh next to National Grid’s substation on the edge of Birmingham, reached commercial operation twenty days after it was energised [[1]](https://www.energy-storage.news/bw-ess-puts-europes-largest-bess-commercial-operation-uk-gb/). In the same week the Campaign to Deliver Affordable Energy Storage, a group of eight short-duration battery developers, published Baringa analysis of Ofgem’s minded-to decision to back 7.6 GW of long-duration storage, eight to 22 hours, under the cap-and-floor scheme [[2]](https://www.ess-news.com/2026/10/30/uk-bess-developers-warn-ldes-cap-and-floor-could-cost-billpayers-gbp-1-6-billion/)[[3]](https://www.baringa.com/en/insights/low-carbon-futures/long-duration-energy-storage/).

Measured against a 4.4 GW reference case, Baringa models two-hour battery revenues 13% lower, around 5 GW less short-duration storage built by 2035, floor top-ups about £110m a year higher on average, and a consumer welfare loss of roughly £1.6bn over 2030–2055 (£1.3bn net across the whole system) [[3]](https://www.baringa.com/en/insights/low-carbon-futures/long-duration-energy-storage/). These are scenarios commissioned by interested parties, not outcomes. Ofgem’s answer is that 7.6 GW sits inside NESO’s recommended range of 2.7–7.7 GW, set at the top end because some projects will shrink or fall away before delivery, and that it has no wish to distort a short-duration market that is building well [[2]](https://www.ess-news.com/2026/10/30/uk-bess-developers-warn-ldes-cap-and-floor-could-cost-billpayers-gbp-1-6-billion/)[[4]](https://www.solarpowerportal.co.uk/energy-storage/ldes-cap-and-floor-support-shortlist-announced-ofgem-says-appropriate-mix-of-technologies).

## One purse

The mechanism matters more than the verdict. A merchant battery earns from price spreads and balancing actions, and those costs end up in bills. A cap-and-floor asset earns in the same markets, and when its income falls short of the floor, consumers make up the difference through a levy [[5]](https://www.energy-uk.org.uk/publications/energy-uk-explains-long-duration-electricity-storage-and-ofgems-cap-and-floor-decisions/). Add more of one and the other’s share shrinks. In this argument, long and short storage are less competing technologies than competing claimants on the same purse.

## The purse next door

There is a larger one. According to the National Audit Office, Britain paid £1.9bn in 2025-26 to turn generators down on one side of grid bottlenecks and up on the other, against £0.6bn in 2018-19; without faster grid upgrades it could reach £6.6–7.8bn a year by 2030 [[6]](https://www.nao.org.uk/wp-content/uploads/2026/09/Upgrading-the-electricity-transmission-network-summary.pdf). Most of it pays northern wind to stop and gas further south to start. This year is running ahead of last: Octopus’s Wasted Wind tracker had 2026 constraint costs passing £1bn two months earlier than in 2025 [[7]](https://www.smartestenergy.com/en_GB/insights/the-informer/cost-of-curtailment-hits-1bn/).

The two figures are different measures, and it is worth saying so: a modelled welfare loss spread over twenty-five years, in a different price basis, against one year’s outturn. As an order of magnitude, though, the whole long-versus-short dispute is smaller than a single year of constraint payments.

## What storage can and cannot reach

A battery behind a constrained boundary can absorb surplus wind until it is full. After that it needs the wire south to have room before it can empty. A battery in the Midlands can replace the gas switched on when Scottish wind is switched off, which is valuable, but the curtailed megawatt-hours never reach it.

What does reach them is demand on the spot. eala’s design puts 3–10 MW of containerised compute at a curtailed renewable node, with six to eight hours of on-site storage sized for long curtailment windows and an orchestration layer that decides, hour by hour, whether a megawatt-hour earns most in the servers, in the store or as a grid service [[8]](https://eala.energy/). Most of that income comes from compute customers, outside the electricity bill. And each curtailed megawatt-hour the site uses is one the system operator no longer pays to switch off. It is not a substitute for new wires; it is something that works while they are built.

## Not less storage

So should the long-duration round be trimmed? We would argue not. Supply swings grow every year as wind connects faster than the network, and storage that is not yet built smooths none of them. Britain needs the batteries and the reservoirs, and sooner rather than later.

The more useful question for anyone building a flexibility model is which of its revenues come from somewhere other than the bill. Those are the ones that add to the pot rather than divide it.

---

## Sources

1. Energy-Storage.News, “BW ESS puts Europe’s largest BESS into commercial operation in the UK”, 3 November 2026. <https://www.energy-storage.news/bw-ess-puts-europes-largest-bess-commercial-operation-uk-gb/>
2. ESS News, “BESS developers warn LDES cap and floor could cost billpayers GBP 1.6 billion”, 30 October 2026. <https://www.ess-news.com/2026/10/30/uk-bess-developers-warn-ldes-cap-and-floor-could-cost-billpayers-gbp-1-6-billion/>
3. Baringa, “Long-duration energy storage: what are the consequences of deploying 7.6 GW through Window 1?”, 27 October 2026. <https://www.baringa.com/en/insights/low-carbon-futures/long-duration-energy-storage/>
4. Solar Power Portal, “LDES cap-and-floor support shortlist announced, Ofgem says ‘appropriate mix’ of technologies”, June 2026. <https://www.solarpowerportal.co.uk/energy-storage/ldes-cap-and-floor-support-shortlist-announced-ofgem-says-appropriate-mix-of-technologies>
5. Energy UK, “Energy UK Explains: Long duration electricity storage and Ofgem’s cap and floor decisions”, 2026. <https://www.energy-uk.org.uk/publications/energy-uk-explains-long-duration-electricity-storage-and-ofgems-cap-and-floor-decisions/>
6. National Audit Office, *Upgrading the electricity transmission network*, September 2026. <https://www.nao.org.uk/wp-content/uploads/2026/09/Upgrading-the-electricity-transmission-network-summary.pdf>
7. SmartestEnergy, “Cost of curtailment hits £1bn” (citing the Wasted Wind tracker), 18 August 2026. <https://www.smartestenergy.com/en_GB/insights/the-informer/cost-of-curtailment-hits-1bn/>
8. eala energy, platform overview. <https://eala.energy/>
