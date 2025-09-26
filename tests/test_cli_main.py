# tests/test_cli_main.py
import subprocess

def test_cli_add():
    """Test the CLI addition command."""
    result = subprocess.run(
        ["python", "-m", "calculator.cli", "add", "2", "3"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "5"

def test_cli_subtract():
    """Test the CLI subtraction command."""
    result = subprocess.run(
        ["python", "-m", "calculator.cli", "subtract", "5", "2"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "3"
