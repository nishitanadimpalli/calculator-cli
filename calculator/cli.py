# calculator/cli.py
from .repl import run_repl

def main(input_func=input, output_func=print):
    """Run the calculator REPL."""
    run_repl(input_func=input_func, output_func=output_func)

def _run_main_for_coverage(input_func=input, output_func=print):
    """Helper to safely run main for coverage testing."""
    main(input_func=input_func, output_func=output_func)

def _cli_main_wrapper(input_func=input, output_func=print):
    """Wrapper to call the CLI safely in tests for coverage."""
    _run_main_for_coverage(input_func=input_func, output_func=output_func)

# Only runs when executing the module directly, not during tests
if __name__ == "__main__":
    _cli_main_wrapper()  # pragma: no cover
