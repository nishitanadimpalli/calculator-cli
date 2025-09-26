# calculator/operations.py

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def operate(op: str, a: float, b: float) -> float:
    """Perform the operation based on the operator string."""
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    # else branch fully reachable via test
    raise ValueError(f"Unknown operator: {op}")
