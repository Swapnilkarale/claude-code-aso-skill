"""Tests for the A/B test planner — sample size + significance math."""

from aso_skill import ABTestPlanner


def test_planner_instantiates():
    planner = ABTestPlanner()
    assert planner is not None


def test_sample_size_increases_as_effect_size_decreases():
    """Smaller MDE => larger n. Sanity-check the math direction."""
    planner = ABTestPlanner()
    big_effect = planner.calculate_sample_size(0.05, 0.20)["sample_size_per_variant"]
    small_effect = planner.calculate_sample_size(0.05, 0.05)["sample_size_per_variant"]
    assert small_effect > big_effect


def test_sample_size_returns_positive_integer():
    planner = ABTestPlanner()
    result = planner.calculate_sample_size(0.05, 0.10)
    n = result["sample_size_per_variant"]
    assert isinstance(n, int)
    assert n > 0
    assert result["total_sample_size"] == n * 2


def test_significance_detects_real_difference():
    """Variant B at 8% vs variant A at 5% with large n should be significant."""
    planner = ABTestPlanner()
    result = planner.calculate_significance(
        variant_a_conversions=500,
        variant_a_visitors=10000,
        variant_b_conversions=800,
        variant_b_visitors=10000,
    )
    assert result["statistical_analysis"]["is_significant_95"] is True


def test_significance_rejects_noise():
    """Identical rates should NOT be flagged significant."""
    planner = ABTestPlanner()
    result = planner.calculate_significance(
        variant_a_conversions=500,
        variant_a_visitors=10000,
        variant_b_conversions=505,
        variant_b_visitors=10000,
    )
    assert result["statistical_analysis"]["is_significant_95"] is False
