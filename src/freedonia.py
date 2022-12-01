""" The Freedonia module.
"""
from decimal import Decimal

PROVINCE_TAX = {
    "Chico": Decimal('.5'),
    "Groucho": Decimal('.7'),
    "Harpo": Decimal('.5'),
    "Zeppo": Decimal('.4')
}
def calculate_tax(
    price: int,
    location: str,
    time: int,
    province_tax: dict = PROVINCE_TAX
) -> float:
    updated_percent = time/Decimal('24.0') * province_tax[location]
    return float(updated_percent * price)
