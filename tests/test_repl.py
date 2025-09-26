# tests/test_repl.py
import pytest
from calculator import repl
from calculator import cli

def test_parse_number_valid():
    assert repl.parse_number(" 3.5 ") == 3.5

def test_evaluate_add():
    assert repl.evaluate('+', '2', '3') == 5

def test_evaluate_div_zero():
    with pytest.raises(ZeroDivisionError):
        repl.evaluate('/', '1', '0')

def test_run_repl_basic():
    inputs = iter(['+', '2', '3', 'exit'])
    outputs = []

    def fake_input(prompt=''):
        return next(inputs)

    def fake_print(*args, **kwargs):
        outputs.append(' '.join(map(str, args)))

    repl.run_repl(input_func=fake_input, output_func=fake_print)
    assert any('Result: 5.0' in line for line in outputs)

def test_run_repl_error_handling():
    """Test exception handling for invalid numbers."""
    inputs = iter(['+', 'a', 'b', 'exit'])
    outputs = []

    def fake_input(prompt=''):
        return next(inputs)

    def fake_print(*args):
        outputs.append(' '.join(map(str, args)))

    repl.run_repl(input_func=fake_input, output_func=fake_print)
    assert any("Error:" in line for line in outputs)

def test_run_repl_unknown_operator():
    """Test exception handling for unknown operator."""
    inputs = iter(['^', '2', '3', 'exit'])
    outputs = []

    def fake_input(prompt=''):
        return next(inputs)

    def fake_print(*args):
        outputs.append(' '.join(map(str, args)))

    repl.run_repl(input_func=fake_input, output_func=fake_print)
    assert any("Error:" in line for line in outputs)

def test_cli_main_integration():
    inputs = iter(['*', '4', '5', 'quit'])
    outputs = []

    def fake_input(prompt=''):
        return next(inputs)

    def fake_print(*args):
        outputs.append(' '.join(map(str, args)))

    cli.main(input_func=fake_input, output_func=fake_print)
    assert any('Result: 20.0' in line for line in outputs)

def test_cli_main_dunder():
    """Ensure the __main__ block runs for coverage."""
    inputs = iter(['+', '1', '2', 'quit'])
    captured = []

    def fake_input(prompt=''):
        return next(inputs)

    def fake_print(*args):
        captured.append(' '.join(map(str, args)))

    cli._run_main_for_coverage(input_func=fake_input, output_func=fake_print)
    assert any("Result: 3.0" in line for line in captured)
