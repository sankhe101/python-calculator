"""The first step of our calculator's calculation engine."""

from decimal import Decimal


def add_numbers(first: str, second: str) -> Decimal:
    """Add two numbers supplied as strings using exact decimal input."""
    return Decimal(first) + Decimal(second)


if __name__ == "__main__":
    result = add_numbers("0.1", "0.2")
    print(result)
