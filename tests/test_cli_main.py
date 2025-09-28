# tests/test_cli_main.py
import sys
import pytest
from calculator import cli

def _run_with_argv(argv):
    """Temporarily replace sys.argv and call cli.main() in-process."""
    old = sys.argv[:]
    try:
        sys.argv[:] = argv
        cli.main()  # prints to stdout which pytest captures
    finally:
        sys.argv[:] = old

def test_cli_add(capfd):
    """Test the CLI addition command in-process so coverage is measured."""
    _run_with_argv(["calculator.cli", "add", "2", "3"])
    out, err = capfd.readouterr()
    assert out.strip() == "5"

def test_cli_subtract(capfd):
    """Test the CLI subtraction command in-process so coverage is measured."""
    _run_with_argv(["calculator.cli", "subtract", "5", "2"])
    out, err = capfd.readouterr()
    assert out.strip() == "3"

def test_divide_float_and_integer_normalization(capfd):
    """Check float result and integer normalization (4/2 -> 2 not 2.0)."""
    _run_with_argv(["calculator.cli", "divide", "7", "2"])
    out, err = capfd.readouterr()
    assert out.strip() == "3.5"

    _run_with_argv(["calculator.cli", "divide", "4", "2"])
    out, err = capfd.readouterr()
    assert out.strip() == "2"

def test_unknown_command_systemexit(capfd):
    """Unknown command should print usage or raise SystemExit with code 2."""
    with pytest.raises(SystemExit) as exc:
        _run_with_argv(["calculator.cli", "pow", "2", "3"])
    out, err = capfd.readouterr()
    assert "Usage:" in out or exc.value.code == 2

def test_missing_args_systemexit(capfd):
    """Missing arguments should print usage or exit with code 2."""
    with pytest.raises(SystemExit) as exc:
        _run_with_argv(["calculator.cli", "add", "2"])  # missing second arg
    out, err = capfd.readouterr()
    assert "Usage:" in out or exc.value.code == 2

def test_invalid_number_systemexit(capfd):
    """Invalid numeric input should print invalid message and usage or exit code 2."""
    with pytest.raises(SystemExit) as exc:
        _run_with_argv(["calculator.cli", "add", "a", "2"])
    out, err = capfd.readouterr()
    assert ("Invalid" in out and "Usage" in out) or exc.value.code == 2

def test_divide_by_zero_systemexit(capfd):
    """Division by zero should produce an Error message or exit with code 1."""
    with pytest.raises(SystemExit) as exc:
        _run_with_argv(["calculator.cli", "divide", "1", "0"])
    out, err = capfd.readouterr()
    assert "Error:" in out or exc.value.code == 1

def test_scientific_notation_parsing(capfd):
    """Ensure scientific notation (1e3) is parsed via float fallback."""
    _run_with_argv(["calculator.cli", "add", "1e3", "2"])
    out, err = capfd.readouterr()
    # depending on implementation, result could be "1002.0"
    assert out.strip() in ("1002", "1002.0", "1002.00")

def test_cli_multiply_and_add_float_normalization(capfd):
    """Cover the multiply branch and an addition that yields a float."""
    _run_with_argv(["calculator.cli", "multiply", "6", "7"])
    out, err = capfd.readouterr()
    assert out.strip() == "42"

    # also cover add with floats that result in integer-looking float
    _run_with_argv(["calculator.cli", "add", "2.0", "3.0"])
    out, err = capfd.readouterr()
    # result might be printed as "5" (normalized) or "5.0"; accept both
    assert out.strip() in ("5", "5.0")

def test_dunder_main_executes(monkeypatch):
    """
    Execute the module as __main__ while replacing the REPL entrypoint
    so it doesn't block — this covers the top-level __main__ path.
    """
    called = []

    # Replace the actual REPL function so it doesn't try to read stdin
    monkeypatch.setattr("calculator.repl.run_repl", lambda *a, **k: called.append(True))

    import runpy, sys
    old_argv = sys.argv[:]
    try:
        # Make sys.argv have only one element so sys.argv[1:]==[] inside the module
        sys.argv[:] = ["python"]
        runpy.run_module("calculator.cli", run_name="__main__")
    finally:
        sys.argv[:] = old_argv

    assert called, "expected repl.run_repl to be invoked via __main__"


