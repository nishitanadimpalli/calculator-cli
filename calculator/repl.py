# calculator/repl.py
from . import operations

def parse_number(s: str) -> float:
    return float(s.strip())

def evaluate(op: str, a: str, b: str) -> float:
    a_num = parse_number(a)
    b_num = parse_number(b)
    return operations.operate(op, a_num, b_num)

def run_repl(input_func=input, output_func=print):
    while True:
        op = input_func("Enter operator (+, -, *, /) or 'exit': ")
        if op.lower() in ['exit', 'quit']:
            break
        a_input = input_func("Enter first number: ")
        b_input = input_func("Enter second number: ")
        try:
            result = evaluate(op, a_input, b_input)
            output_func(f"Result: {result}")
        except Exception as e:
            output_func(f"Error: {e}")
