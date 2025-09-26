# tests/test_cli_main.py
from calculator import cli

def test_cli_main_line_coverage_safe():
    """Cover CLI main safely without blocking stdin."""

    # Fake input/output so REPL exits immediately
    def fake_input(prompt=''):
        return 'exit'  # stops the REPL immediately

    def fake_print(*args):
        pass

    # Call CLI wrapper with fake input/output
    cli._cli_main_wrapper(input_func=fake_input, output_func=fake_print)
