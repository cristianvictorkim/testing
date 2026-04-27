import pytest

from app.discounts import calculate_total


def test_calculate_total_for_premium_customer_successfully():
    result = calculate_total(1000, "premium")

    assert result.discount_rate == 0.10
    assert result.discount_amount == 100
    assert result.total == 900


def test_calculate_total_rejects_negative_subtotal():
    with pytest.raises(ValueError, match="subtotal no puede ser negativo"):
        calculate_total(-1, "regular")


def test_calculate_total_for_zero_subtotal_edge_case():
    result = calculate_total(0, "vip")

    assert result.discount_amount == 0
    assert result.total == 0


def test_calculate_total_normalizes_customer_type():
    result = calculate_total(500, " VIP ")

    assert result.customer_type == "vip"
    assert result.discount_amount == 100
    assert result.total == 400
