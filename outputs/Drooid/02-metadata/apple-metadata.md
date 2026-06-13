# Drooid — Apple App Store Metadata (Copy-Paste Ready)

**App:** Drooid (App ID 6593684010) · **Target:** App Store Connect
**All fields validated against Apple character limits ✅**
**Data date:** 2026-06-12

> ⚠️ **One thing to confirm first:** the iTunes API returns your **title** as `Drooid: News from all sides` but does *not* expose your current **subtitle**. Check App Store Connect for what's in the subtitle field today before overwriting it. Recommendations below assume you're refreshing both.

---

## RECOMMENDED (primary)

### Title — `30` char limit
```
Drooid: Balanced AI News
```
**24/30** ✅ · Adds high-value *balanced* + *AI* (both higher-volume than "from all sides"). Keeps brand first.

### Subtitle — `30` char limit
```
Unbiased News from All Sides
```
**28/30** ✅ · Preserves your "all sides" tagline equity + adds *unbiased*. No word overlaps the title.

### Keywords — `100` char limit (comma-separated, **no spaces**)
```
bias,media,perspective,summaries,headlines,aggregator,politics,world,factcheck,left,right,center
```
**96/100** ✅ · 12 terms, **zero** repeats from title/subtitle (maximizes Apple auto-combinations).

### Promotional Text — `170` char limit (updatable anytime, not indexed)
```
See every news story from Left, Center & Right — summarized by AI. Understand the full picture in minutes, not hours.
```
**117/170** ✅

### Description — `4000` char limit (⚠️ not indexed by Apple — pure conversion)
```
Drooid: Balanced News and Multiple Perspectives, Summarized by AI

Most people get news through social feeds — reactive, algorithm-driven, and usually framed from a single side. Drooid offers a better way to stay informed.

Drooid is an AI-powered news app that helps you understand the full picture. Instead of endless headlines, Drooid gives you clear, concise summaries showing how Left, Center, and Right outlets cover the same story. You see what happened, why it matters, and how the narratives differ.

WHY READERS CHOOSE DROOID
• Balanced news coverage across every viewpoint
• Short, high-signal AI news summaries
• Transparent citations and direct source links
• In-depth AI news analysis on major stories
• Historical and factual context when it helps
• A calm, distraction-free reading experience

Every summary links straight to the original articles, so you can verify claims, explore deeper, and read from trusted publishers.

HOW DROOID WORKS
1. Drooid collects articles from reputable publishers and outlets.
2. AI generates structured summaries from multiple sources.
3. Differing perspectives are identified and shown side by side.
4. Relevant historical and factual context is added when useful.
5. Each summary includes citations and links to sources.
6. You can open deeper AI-powered analysis of major stories.

WHAT YOU CAN DO
• Read short AI summaries from multiple perspectives
• Compare coverage across publishers, left to right
• Open the original news articles in one tap
• Explore in-depth AI analysis
• Follow topics and people you care about
• Search stories, events, and discussions
• Comment, share, and join the community feed
• Save stories to read later

A SMARTER NEWS EXPERIENCE
Drooid is built for readers who value clarity, transparency, and context. If you want to compare viewpoints, check media bias, verify claims, and move past one-sided coverage, Drooid is made for you.

Download Drooid and understand the complete picture — faster.

Terms of Use: https://drooid.social/terms-of-use
Privacy Policy: https://drooid.social/privacy
```
**2076/4000** ✅

---

## CONSERVATIVE alternative (if you want to keep the current title)

If the team wants to preserve brand recognition of the existing title, run this instead and move the new keywords into subtitle:

| Field | Value | Chars |
|---|---|---|
| Title | `Drooid: News from all sides` | 27/30 |
| Subtitle | `Balanced & Unbiased AI News` | 27/30 |
| Keywords | `bias,media,perspective,summaries,headlines,aggregator,politics,world,factcheck,left,right,center` | 96/100 |

This still injects *balanced, unbiased, AI, summaries* — just via subtitle instead of title. **Weaker** than the primary (title weight > subtitle weight) but lower-risk for brand.

---

## ▶️ Recommended approach: A/B test it

Don't guess — let Apple's data decide. Run a **Product Page Optimization (PPO)** test in App Store Connect:
- **Control:** current title/subtitle
- **Treatment:** Primary recommendation above
- **Metric:** impressions → product page views → conversion rate
- **Duration:** until statistical significance (typically 2–4 weeks at your traffic; with 54 ratings, expect the longer end)

> Note: PPO tests *icon/screenshots/preview*, not the keyword field directly — but you can ship the new title/subtitle as a treatment and watch conversion. Keyword-ranking impact is measured separately via your search impression data after the change goes live.

---

## Implementation checklist

- [ ] Confirm current subtitle in App Store Connect before overwriting
- [ ] Paste Title → App Information
- [ ] Paste Subtitle → App Information
- [ ] Paste Keywords → App Store Connect → Keywords field (verify no trailing spaces)
- [ ] Paste Promotional Text (can update without app review)
- [ ] Paste Description
- [ ] Submit (metadata-only changes don't require a new build, but do require review)
- [ ] After live: monitor App Store Connect → Analytics → Search impressions for Tier 1 terms
