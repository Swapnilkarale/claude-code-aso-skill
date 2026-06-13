# ⭐ Drooid — ASO Master Action Plan

**App:** Drooid: News from all sides · App ID `6593684010` · `social.drooid`
**Focus:** Maximize keyword discovery · **Platforms:** Apple + Google
**Generated:** 2026-06-12 · **All metadata validated against character limits ✅**

---

## TL;DR — what to do this week

1. **Apple title** `Drooid: News from all sides` → **`Drooid: Balanced AI News`** (adds 2 high-value keywords)
2. **Apple keyword field** → `bias,media,perspective,summaries,headlines,aggregator,politics,world,factcheck,left,right,center` (96/100, currently almost certainly under-used)
3. **Own the "AI summaries" gap** — no competitor leads with it, and it's genuinely Drooid's product
4. **A/B test** the title change via App Store Connect PPO before fully committing

**The single biggest lever:** your description is *not* indexed by Apple. Right now your searchable keywords live only in title + subtitle + the 100-char field. Make those three count.

---

## ⚠️ Volume Reality Check — real Apple Search Ads data (2026-06-12)

We pulled live Search Popularity dots (1–5) from Apple Search Ads. The result **reframes the whole strategy**:

| Keyword | Dots | Verdict |
|---|---|---|
| news | 4 | High volume, but generic + dominated by Apple/Google News |
| ai | 4 | High, but means ChatGPT-type apps, not news |
| ai news | 1 | The exact phrase is barely searched |
| balanced news / unbiased news / media bias | 1 each | Niche intent terms have almost no volume |
| **ground news** (competitor brand) | **3** | 🔑 More searched than every generic intent term combined |

**Conclusion: demand in this niche is _branded_, not _generic_.** People search "Ground News" by name; almost nobody searches "balanced news." So **keyword ASO has a low ceiling for Drooid** — you can't farm volume that isn't there.

**Revised priority order:**
1. 🥇 **Build the "Drooid" brand** so *it* becomes the search term (PR, sponsorships, word-of-mouth — how Ground News won). This is marketing, not ASO.
2. 🥈 **Maximize conversion + ratings** on the scarce impressions you get (54 → 500 ratings matters more than any keyword tweak).
3. 🥉 **(If paid, later) Conquest "Ground News" in Apple Search Ads** — 3 dots of high-intent traffic.
4. Metadata below still worth doing (keep `News` + `AI` — the only 4-dot words in your niche), but treat the title's job as **clarity/conversion**, not keyword farming.

---

## Current state (verified live data)

| Metric | Value | Read |
|---|---|---|
| Rating | ⭐ 4.39 (54 ratings) | Quality is good; **volume is the constraint** |
| Title | "Drooid: News from all sides" | Brand + weak-search tagline |
| Category | News · Magazines & Newspapers | Correct |
| Languages | English only | Localization = future upside |
| vs Ground News | 54 vs 44,058 ratings | Flank, don't charge |

---

## Phase 1 — Metadata (do now · ~1 hour) 🔴 Highest impact

**Apple** → full strings in [`02-metadata/apple-metadata.md`](02-metadata/apple-metadata.md)
- [ ] Confirm current subtitle in App Store Connect (API doesn't expose it)
- [ ] Update Title → `Drooid: Balanced AI News` (24/30)
- [ ] Update Subtitle → `Unbiased News from All Sides` (28/30)
- [ ] Update Keyword field → `bias,media,perspective,summaries,headlines,aggregator,politics,world,factcheck,left,right,center` (96/100)
- [ ] Update Promotional Text + Description (conversion)
- [ ] Submit for review

**Google** → full strings in [`02-metadata/google-metadata.md`](02-metadata/google-metadata.md)
- [ ] Confirm current Play listing text + category (News & Magazines)
- [ ] Update Title → `Drooid: Balanced AI News from All Sides` (39/50)
- [ ] Update Short description (67/80)
- [ ] Update Full description (keyword-weighted, 2343/4000)
- [ ] Save & submit

## Phase 2 — Validate with data (week 1–4) 🟡

- [ ] Launch App Store Connect **Product Page Optimization** test: current title vs `Drooid: Balanced AI News`
- [ ] Baseline your Tier-1 keyword ranks *before* the change (so you can measure lift)
- [ ] Track App Store Connect → Search impressions for: `ai news`, `balanced news`, `unbiased news`, `news summary`
- [ ] Track Play Console → Acquisition → Search

## Phase 3 — Conversion & reviews (ongoing) 🟢

- [ ] Make screenshot #1 say the value prop in 5 words ("AI summaries. Every side.") — first screenshot drives most conversion
- [ ] Add an in-app review prompt after a positive moment (reading 3+ summaries) — your 54-rating count is the real growth ceiling; more ratings → higher rank + conversion
- [ ] Respond to App Store reviews (templates can be generated on request)

## Phase 4 — Expansion (later) 🔵

- [ ] Add localized listings: `en-GB`, `en-AU`, `en-IN` (free keyword reach, English-only effort)
- [ ] Re-run this audit each quarter or after any major feature launch
- [ ] Consider an "In-Depth AI Analysis" feature callout in metadata once it's a headline feature

---

## Deliverables in this folder

| File                             | What's in it                                    |
| -------------------------------- | ----------------------------------------------- |
| `00-MASTER-ACTION-PLAN.md`       | ⭐ This file                                     |
| `01-research/keyword-list.md`    | Prioritized keywords (3 tiers) + allocation map |
| `01-research/competitor-gaps.md` | 4 gaps vs Ground News / AllSides / SmartNews    |
| `02-metadata/apple-metadata.md`  | Copy-paste App Store Connect fields (validated) |
| `02-metadata/google-metadata.md` | Copy-paste Play Console fields (validated)      |
| `FINAL-REPORT.md`                | Executive summary                               |

---

## Honest caveats

- **Search volumes are estimates.** No public API exposes App Store search volume. *Relative* priorities are sound; exact numbers need a paid tool (AppTweak/Sensor Tower) or your own post-change impression data.
- **Title changes carry brand risk.** That's why Phase 2 is an A/B test, not a blind commit. A conservative title-preserving option is in the Apple metadata file.
- **ASO compounds with ratings.** With 54 ratings, your biggest non-metadata lever is simply *getting more reviews*. Metadata gets you found; ratings get you ranked and installed.
