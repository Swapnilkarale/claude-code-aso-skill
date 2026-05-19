"""Tests for the ASO scorer."""

from aso_skill import ASOScorer, calculate_aso_score


METADATA_OK = {
    "title_keyword_count": 2,
    "title_length": 28,
    "description_length": 2200,
    "description_quality": 0.8,
    "keyword_density": 4.5,
}
RATINGS_OK = {"average_rating": 4.6, "total_ratings": 8500, "recent_ratings_30d": 350}
KEYWORDS_OK = {"top_10": 6, "top_50": 18, "top_100": 30, "improving_keywords": 8}
CONVERSION_OK = {
    "impression_to_install": 0.06,
    "downloads_last_30_days": 12000,
    "downloads_trend": "up",
}


def test_weights_sum_to_one_hundred():
    assert sum(ASOScorer.WEIGHTS.values()) == 100


def test_score_is_within_zero_to_one_hundred():
    result = calculate_aso_score(METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK)
    assert 0 <= result["overall_score"] <= 100


def test_breakdown_has_four_components():
    result = calculate_aso_score(METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK)
    breakdown = result["score_breakdown"]
    assert set(breakdown.keys()) == set(ASOScorer.WEIGHTS.keys())


def test_breakdown_weights_match_constants():
    result = calculate_aso_score(METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK)
    for component, expected_weight in ASOScorer.WEIGHTS.items():
        assert result["score_breakdown"][component]["weight"] == expected_weight


def test_health_status_is_present():
    result = calculate_aso_score(METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK)
    assert isinstance(result["health_status"], str)
    assert len(result["health_status"]) > 0


def test_zero_inputs_produce_low_score():
    zero_metadata = {
        "title_keyword_count": 0,
        "title_length": 0,
        "description_length": 0,
        "keyword_density": 0,
    }
    zero_ratings = {"average_rating": 0, "total_ratings": 0, "recent_ratings_30d": 0}
    zero_keywords = {"top_10": 0, "top_50": 0, "top_100": 0, "improving_keywords": 0}
    zero_conversion = {
        "impression_to_install": 0,
        "downloads_last_30_days": 0,
        "downloads_trend": "down",
    }
    result = calculate_aso_score(zero_metadata, zero_ratings, zero_keywords, zero_conversion)
    assert result["overall_score"] <= 30


def test_high_inputs_produce_high_score():
    great_metadata = {
        "title_keyword_count": 2,
        "title_length": 28,
        "description_length": 3500,
        "description_quality": 0.95,
        "keyword_density": 4.0,
    }
    great_ratings = {"average_rating": 4.9, "total_ratings": 50000, "recent_ratings_30d": 2000}
    great_keywords = {"top_10": 12, "top_50": 25, "top_100": 50, "improving_keywords": 10}
    great_conversion = {
        "impression_to_install": 0.15,
        "downloads_last_30_days": 20000,
        "downloads_trend": "up",
    }
    result = calculate_aso_score(great_metadata, great_ratings, great_keywords, great_conversion)
    assert result["overall_score"] >= 60


def test_recommendations_field_present():
    result = calculate_aso_score(METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK)
    assert "recommendations" in result
    assert isinstance(result["recommendations"], list)


def test_scorer_class_matches_convenience_function():
    direct = ASOScorer().calculate_overall_score(
        METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK
    )
    via_func = calculate_aso_score(METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK)
    assert direct["overall_score"] == via_func["overall_score"]


def test_weighted_contributions_sum_to_overall():
    result = calculate_aso_score(METADATA_OK, RATINGS_OK, KEYWORDS_OK, CONVERSION_OK)
    contributions = sum(c["weighted_contribution"] for c in result["score_breakdown"].values())
    assert abs(contributions - result["overall_score"]) < 0.5
