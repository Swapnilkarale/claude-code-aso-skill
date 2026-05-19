"""Tests for the metadata optimizer and character-limit validation."""

import pytest

from aso_skill import MetadataOptimizer


def test_invalid_platform_raises():
    with pytest.raises(ValueError):
        MetadataOptimizer(platform="invalid")


def test_apple_title_at_limit_is_valid():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"title": "X" * 30})
    assert result["is_valid"] is True
    assert result["field_status"]["title"]["is_valid"] is True


def test_apple_title_over_limit_is_invalid():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"title": "X" * 31})
    assert result["is_valid"] is False
    assert "exceeds limit" in result["errors"][0]


def test_apple_subtitle_thirty_chars():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"subtitle": "X" * 30})
    assert result["is_valid"] is True


def test_apple_keywords_one_hundred_chars():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"keywords": "X" * 100})
    assert result["is_valid"] is True


def test_apple_keywords_over_one_hundred():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"keywords": "X" * 101})
    assert result["is_valid"] is False


def test_apple_description_four_thousand():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"description": "X" * 4000})
    assert result["is_valid"] is True


def test_apple_description_over_limit():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"description": "X" * 4001})
    assert result["is_valid"] is False


def test_google_title_fifty_chars():
    optimizer = MetadataOptimizer("google")
    result = optimizer.validate_character_limits({"title": "X" * 50})
    assert result["is_valid"] is True


def test_google_short_description_eighty_chars():
    optimizer = MetadataOptimizer("google")
    result = optimizer.validate_character_limits({"short_description": "X" * 80})
    assert result["is_valid"] is True


def test_google_full_description_four_thousand():
    optimizer = MetadataOptimizer("google")
    result = optimizer.validate_character_limits({"full_description": "X" * 4000})
    assert result["is_valid"] is True


def test_unknown_field_generates_warning():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"unknown_field": "anything"})
    assert any("Unknown field" in w for w in result["warnings"])


def test_empty_value_under_limit():
    optimizer = MetadataOptimizer("apple")
    result = optimizer.validate_character_limits({"title": ""})
    assert result["is_valid"] is True
    assert result["field_status"]["title"]["length"] == 0


def test_keyword_density_in_reasonable_range():
    optimizer = MetadataOptimizer("apple")
    text = "Build your task list with our task manager app. Tasks made simple."
    densities = optimizer.calculate_keyword_density(text, ["task"])
    density = densities["keyword_densities"]["task"]
    assert density["occurrences"] >= 1
    assert 0 <= density["density_percentage"] <= 100
