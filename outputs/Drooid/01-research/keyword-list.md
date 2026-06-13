# Drooid — Keyword Research & Opportunity Map

**App:** Drooid: News from all sides (App ID 6593684010)
**Category:** News (primary) · Magazines & Newspapers
**Goal of this refresh:** Maximize keyword discovery (organic search reach)
**Data date:** 2026-06-12 · Source: iTunes Search/Lookup API (verified live)

---

## How App Store search indexing works (read first)

| Field | Apple indexes? | Google indexes? | Lever strength |
|---|---|---|---|
| Title | ✅ Yes (highest weight) | ✅ Yes (highest weight) | 🔴 Critical |
| Subtitle (Apple) / Short desc (Google) | ✅ Yes (high) | ✅ Yes (high) | 🔴 Critical |
| Keyword field (Apple only, 100 chars) | ✅ Yes | n/a | 🔴 Critical |
| Description | ❌ **No** | ✅ Yes (medium) | 🟢 Apple: conversion only · Google: keywords |

**Key implication:** On **Apple**, your *only* keyword levers are Title + Subtitle + the 100-char keyword field. The description does **not** help you rank. On **Google**, the full description *is* indexed, so it carries real keyword weight.

Apple also **auto-combines** words across these fields (e.g. "balanced" + "news" → ranks for "balanced news") — so you should **never repeat a word** across title/subtitle/keywords, and you don't need to store multi-word phrases.

---

## Keyword priority tiers

Volume/competition below are **directional estimates** for the US News category (no public API exposes exact App Store search volume — see Data Confidence note at the bottom). Priority = (relevance × volume) ÷ competition, weighted for Drooid's actual product.

### 🟢 Tier 1 — Drooid's "win zone" (high relevance, competitors UNDERWEIGHT these)

These are the terms Drooid should own because they match the product AND rivals aren't fully targeting them.

| Keyword | Est. volume | Competition | Why Drooid can win |
|---|---|---|---|
| `ai news` | High | Medium | **Drooid's core differentiator.** Ground News & AllSides do *not* lead with "AI". Drooid is genuinely AI-summary-first. Biggest single opportunity. |
| `news summary` / `news summaries` | Medium-High | Low-Med | Drooid's product *is* summaries. Almost no balanced-news rival targets this term. |
| `ai news summary` | Medium | **Low** | Long-tail, near-zero competition, perfectly on-product. Easy ranking. |
| `balanced news` | Medium-High | Medium | AllSides literally names itself this. Drooid must contest it — it's the category's defining term. |
| `unbiased news` | High | Medium | High intent, directly on-message ("from all sides"). |
| `news from all sides` | Medium | Low | Drooid's existing tagline — keep the equity, it's low-competition. |

### 🟡 Tier 2 — Category core (must-have table stakes)

High volume, higher competition — you won't rank #1 fast, but you must be present to capture mid-funnel search.

| Keyword | Est. volume | Competition | Notes |
|---|---|---|---|
| `news` | Very High | Very High | Implicit via title; don't over-invest. |
| `news app` | High | High | Captured via "news" + combinations. |
| `breaking news` | Very High | Very High | SmartNews/AP own this; secondary for Drooid. |
| `media bias` | Medium-High | Medium | **Ground News owns this.** Contest via keyword field, not title. |
| `bias checker` / `bias` | Medium | Medium | Ground News territory; include in keyword field. |
| `political news` | High | High | Relevant (Left/Center/Right framing). |
| `world news` / `global news` | High | High | Keyword-field candidates. |

### 🔵 Tier 3 — Long-tail (low competition, high conversion, fast wins)

3–4 word phrases. Lower volume each, but they **add up**, convert better, and Drooid can rank quickly.

- `ai news summary app`
- `left center right news`
- `compare news coverage`
- `news from both sides`
- `unbiased news app`
- `media bias checker`
- `news without bias`
- `multiple perspectives news`
- `news bias ratings`
- `fact check news app`

---

## Recommended keyword allocation (what goes where)

> Built so **no word repeats** across fields (maximizes Apple's auto-combination reach). Full copy-paste strings are in `02-metadata/`.

**Apple**
- **Title** → `Drooid: Balanced AI News` — captures *balanced, ai, news* (+ brand)
- **Subtitle** → `Unbiased News from All Sides` — adds *unbiased, from, all, sides*
- **Keyword field (96/100)** → `bias,media,perspective,summaries,headlines,aggregator,politics,world,factcheck,left,right,center`
- **Auto-combinations this unlocks:** "balanced news", "ai news", "unbiased news", "news summaries", "media bias", "balanced ai news", "news from all sides", "political news", "world news", "left right center" … from just three fields.

**Google**
- **Title (39/50)** → `Drooid: Balanced AI News from All Sides`
- **Short desc (67/80)** → `AI news summaries showing left, center & right views on every story`
- **Full description** → repeat the Tier 1–2 terms 3–5× naturally (Google indexes this). See `02-metadata/google-metadata.md`.

---

## Data confidence

- ✅ **Verified (live API):** Drooid + competitor names, categories, ratings, descriptions, update dates.
- 🟡 **Estimated (no public source):** search volumes & competition scores. Apple/Google do not expose App Store search volume publicly. For exact numbers, validate with a paid tool (AppTweak, Sensor Tower, AppFollow) — but the *relative* priorities above hold regardless.
- ▶️ **Action:** Treat Tier 1 as the proven-safe bets. Use App Store Connect's own impression/conversion data after the change ships to confirm.

---
*Next: see `competitor-gaps.md` for why these gaps exist, and `02-metadata/` for copy-paste strings.*
