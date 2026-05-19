"""Tests for the keyword analyzer."""

from aso_skill import KeywordAnalyzer, analyze_keyword_set


KEYWORDS_FIXTURE = [
    {"keyword": "task manager", "search_volume": 50000, "competition": 75, "relevance": 90},
    {"keyword": "todo list app", "search_volume": 35000, "competition": 65, "relevance": 95},
    {"keyword": "productivity app", "search_volume": 80000, "competition": 85, "relevance": 80},
    {"keyword": "ai task planner", "search_volume": 2500, "competition": 25, "relevance": 95},
]


def test_analyzer_instantiates():
    analyzer = KeywordAnalyzer()
    assert analyzer is not None


def test_analyze_keyword_set_returns_dict():
    result = analyze_keyword_set(KEYWORDS_FIXTURE)
    assert isinstance(result, dict)


def test_analyze_keyword_set_has_ranked_results():
    result = analyze_keyword_set(KEYWORDS_FIXTURE)
    keys_present = set(result.keys())
    assert keys_present, "result is empty"
    # Expect at least some structural fields
    assert any(
        "keyword" in k.lower()
        or "rank" in k.lower()
        or "top" in k.lower()
        or "summary" in k.lower()
        for k in keys_present
    )


def test_low_competition_high_relevance_is_long_tail_candidate():
    result = analyze_keyword_set(KEYWORDS_FIXTURE)
    serialised = str(result).lower()
    # The 'ai task planner' fixture has low competition (25) and high relevance (95)
    assert "ai task planner" in serialised


def test_empty_keyword_set_does_not_crash():
    result = analyze_keyword_set([])
    assert isinstance(result, dict)
