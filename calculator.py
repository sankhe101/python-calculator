"""Safe decimal arithmetic parser, independent of the interface."""
import re
from decimal import Decimal, DecimalException, localcontext


class CalculationError(ValueError):
    """An expression that needs correction."""


TOKEN = re.compile(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?|[+*/()%\-]")


class Parser:
    def __init__(self, text):
        self.tokens = []
        position = 0
        while position < len(text):
            if text[position].isspace():
                position += 1
                continue
            match = TOKEN.match(text, position)
            if not match:
                raise CalculationError(f"Unsupported character at position {position + 1}.")
            self.tokens.append(match.group())
            position = match.end()
        self.position = 0

    def peek(self):
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def take(self):
        token = self.peek()
        self.position += 1
        return token

    def expression(self):
        value = self.term()
        while self.peek() in ("+", "-"):
            operator = self.take()
            other = self.term()
            value = value + other if operator == "+" else value - other
        return value

    def term(self):
        value = self.unary()
        while self.peek() in ("*", "/"):
            operator = self.take()
            other = self.unary()
            if operator == "/" and other == 0:
                raise CalculationError("Cannot divide by zero.")
            value = value * other if operator == "*" else value / other
        return value

    def unary(self):
        if self.peek() in ("+", "-"):
            operator = self.take()
            value = self.unary()
            return -value if operator == "-" else value
        value = self.primary()
        while self.peek() == "%":
            self.take()
            value /= Decimal(100)
        return value

    def primary(self):
        token = self.take()
        if token == "(":
            value = self.expression()
            if self.take() != ")":
                raise CalculationError("Missing closing parenthesis.")
            return value
        if token is None or token in "+-*/()%":
            raise CalculationError("Enter a number or a parenthesized expression.")
        return Decimal(token)


def calculate(expression: str) -> Decimal:
    if not expression.strip():
        raise CalculationError("Enter an expression first.")
    if len(expression) > 1000:
        raise CalculationError("Expression is too long (maximum 1000 characters).")
    text = expression.replace("×", "*").replace("÷", "/").replace("−", "-")
    try:
        with localcontext() as context:
            context.prec = 50
            parser = Parser(text)
            result = parser.expression()
            if parser.peek() is not None:
                raise CalculationError("Unexpected input. Check operators and parentheses.")
            if not result.is_finite():
                raise CalculationError("Result is outside the supported range.")
            return result
    except (DecimalException, RecursionError) as error:
        raise CalculationError("Number or expression is outside the supported range.") from error


def format_result(value: Decimal) -> str:
    """Round display to 12 significant digits and remove trailing zeros."""
    if value == 0:
        return "0"
    with localcontext() as context:
        context.prec = 12
        rounded = +value
    if -6 <= rounded.adjusted() < 12:
        text = format(rounded, "f")
        return text.rstrip("0").rstrip(".") if "." in text else text
    mantissa, exponent = format(rounded, "e").split("e")
    if "." in mantissa:
        mantissa = mantissa.rstrip("0").rstrip(".")
    return f"{mantissa}e{int(exponent):+d}"


def add_numbers(first: str, second: str) -> Decimal:
    """Our original learning example."""
    with localcontext() as context:
        context.prec = 50
        return Decimal(first) + Decimal(second)


if __name__ == "__main__":
    print(format_result(calculate("0.1 + 0.2")))
