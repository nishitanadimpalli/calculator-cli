# calculator/cli.py
import sys
from .repl import run_repl
from .operations import add, subtract, multiply, divide

USAGE = "Usage: python -m calculator.cli <add|subtract|multiply|divide> a b"

def _parse_number(s: str):
    """Parse integer when possible, else float."""
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        return float(s)

def main(input_func=None, output_func=print):
    """
    If input_func is provided -> run interactive REPL (used by tests).
    Otherwise, if command-line args are present, run command-mode.
    Else fallback to REPL.
    """
    # If tests call main with injected IO, respect that
    if input_func is not None:
        run_repl(input_func=input_func, output_func=output_func)
        return

    # Otherwise check for CLI-style args: python -m calculator.cli add 2 3
    args = sys.argv[1:]
    if args:
        cmd = args[0].lower()
        ops = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
        }

        if cmd not in ops:
            print(USAGE)
            sys.exit(2)

        if len(args) < 3:
            print(USAGE)
            sys.exit(2)

        try:
            a = _parse_number(args[1])
            b = _parse_number(args[2])
        except Exception:
            print("Invalid number(s).", USAGE)
            sys.exit(2)

        try:
            result = ops[cmd](a, b)
        except Exception as exc:
            print(f"Error: {exc}")
            sys.exit(1)

        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(result)
        return

    # No injected IO and no args => run REPL (original behavior)
    run_repl()

def _run_main_for_coverage(input_func=input, output_func=print):
    """Helper to safely run main for coverage testing."""
    main(input_func=input_func, output_func=output_func)

def _cli_main_wrapper(input_func=input, output_func=print):
    """Wrapper to call the CLI safely in tests for coverage."""
    _run_main_for_coverage(input_func=input_func, output_func=output_func)

if __name__ == "__main__":
    # When run as a module, main() will check sys.argv and run command-mode or REPL.
    main()
