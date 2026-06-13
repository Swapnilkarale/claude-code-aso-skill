# Drooid — Search Volume Scorecard (Apple Search Ads)

**Goal:** Get real Apple search volume (Search Popularity) for the recommended keywords.
**Source:** Apple Search Ads Advanced — the only first-party volume signal Apple provides.
**Created:** 2026-06-12 · **Results recorded:** 2026-06-12

---

## ✅ ACTUAL RESULTS (live ASA data, US storefront)

Controls (to confirm setup): `instagram` 5 · `youtube` 5 · `weather` 4 → setup verified working.

| Keyword | Dots | Read |
|---|---|---|
| news | 4 | High but generic (Apple/Google News dominate) |
| ai | 4 | High but means AI-assistant apps, not news |
| ai news | 1 | Exact phrase barely searched |
| balanced news | 1 | Niche term, near-zero volume |
| unbiased news | 1 | Near-zero volume |
| media bias | 1 | Near-zero volume |
| **ground news** | **3** | 🔑 Competitor brand out-searches every generic term |

**Verdict:** Demand in this niche is **branded, not generic**. Keyword ASO has a low ceiling for Drooid. Growth levers shift to **brand-building → conversion/ratings → (optional) paid competitor conquesting**. Keep `News` + `AI` in metadata (only 4-dot words); don't over-invest in 1-dot phrases. See `00-MASTER-ACTION-PLAN.md` → "Volume Reality Check".

---

## How Apple shows volume

- In the **ASA Advanced campaign manager**, each keyword gets a **Search Popularity score shown as 1–5 blue dots** (5 = most searched).
- Paid tools / the free Chrome extension convert those dots to a **5–100 scale** (100 = highest volume).
- ⚠️ **Oct 2025 change:** Apple's API no longer returns popularity for keywords scoring **< 35** (≈ below ~2 dots). A blank in a tool = genuinely low volume, not a fetch error. In the manager UI you still see the dots.

## How to read the scores

| Dots | ~5–100 score | Meaning | Action for Drooid |
|---|---|---|---|
| ●●●●● | ~80–100 | Very high volume, high competition | Worth targeting only if relevant; expect slow ranking |
| ●●●● | ~60–80 | High | Strong target if on-product |
| ●●● | ~45–60 | Solid mid-volume | **Sweet spot** — target these |
| ●● | ~35–45 | Niche / long-tail | Good for fast wins, lower traffic |
| ● | < 35 | Very low / may show blank | Keep only if perfectly on-brand |

---

## Step-by-step

1. `searchads.apple.com` → sign in (Apple ID with Drooid access) → **Apple Search Ads Advanced**
2. **Create Campaign** → select **Drooid** → country **United States**
3. Continue to **Ad Group → Keywords**
4. Paste each keyword below → read the **blue dots**
5. Record the dots in the table → **do not submit** the campaign (save draft / exit). No charge unless ads run.
6. *(Optional)* Install Chrome extension **"Apple Ads Benchmarks & KW Popularity"** to see 5–100 numbers.

---

## Scorecard — fill in the Dots / Score columns

### 🟢 Tier 1 — Win zone (test these FIRST — strategy depends on them)

| Keyword | Dots (1–5) | Score (5–100) | Notes |
|---|---|---|---|
| ai news | | | Drooid's core differentiator |
| balanced news | | | Key contested term (AllSides) |
| unbiased news | | | High intent |
| news summary | | | Open lane vs competitors |
| ai news summary | | | Long-tail, expect low comp |
| news from all sides | | | Current tagline — is it worth the title space? |

### 🟡 Tier 2 — Category core

| Keyword | Dots (1–5) | Score (5–100) | Notes |
|---|---|---|---|
| news app | | | |
| media bias | | | Ground News territory |
| political news | | | |
| world news | | | |
| breaking news | | | Expect very high + very competitive |
| bias checker | | | |

### 🔵 Tier 3 — Long-tail (fast-win candidates)

| Keyword | Dots (1–5) | Score (5–100) | Notes |
|---|---|---|---|
| ai news summary app | | | |
| left center right news | | | |
| compare news coverage | | | |
| unbiased news app | | | |
| media bias checker | | | |
| multiple perspectives news | | | |

---

## Decision rules after you score

- **`ai news` and `balanced news` ≥ 3 dots** → ship the recommended title `Drooid: Balanced AI News`. Confirmed high-value.
- **`news from all sides` ≤ 2 dots** → data proof the current title wastes space; move it to subtitle or drop it.
- **Any Tier-1 term at 4–5 dots** → make sure it's in title or subtitle (highest-weight fields), not just the keyword field.
- **Tier-3 terms at 2–3 dots** → cheap wins; ensure their component words are covered so Apple's auto-combination catches them.
- **Re-rank the keyword field** (`02-metadata/apple-metadata.md`) so the highest-scoring distinct terms fill the 100 chars first.

---

## If you'd rather not set up ASA

- **Paid one-click:** AppTweak, Sensor Tower, AppFollow, MobileAction (all have free trials) show volume + difficulty per keyword.
- **Manual proxy:** on an iPhone, type each seed into App Store Search — the autocomplete order reflects demand (directional only).

*Once you've filled in the dots, share them back and I'll re-prioritize the keyword field and finalize the title recommendation against real numbers.*
