from dataclasses import dataclass


@dataclass(frozen=True)
class DiscountResult:
    subtotal: float
    customer_type: str
    discount_rate: float
    discount_amount: float
    total: float


DISCOUNT_RATES = {
    "regular": 0.00,
    "premium": 0.10,
    "vip": 0.20,
}


def calculate_total(subtotal: float, customer_type: str) -> DiscountResult:
    """Calculate the final total for a purchase after applying a customer discount."""
    if subtotal < 0:
        raise ValueError("El subtotal no puede ser negativo.")

    normalized_type = customer_type.strip().lower()
    if normalized_type not in DISCOUNT_RATES:
        raise ValueError("Tipo de cliente invalido.")

    discount_rate = DISCOUNT_RATES[normalized_type]
    discount_amount = round(subtotal * discount_rate, 2)
    total = round(subtotal - discount_amount, 2)

    return DiscountResult(
        subtotal=subtotal,
        customer_type=normalized_type,
        discount_rate=discount_rate,
        discount_amount=discount_amount,
        total=total,
    )
