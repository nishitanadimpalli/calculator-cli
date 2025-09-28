# Calculator CLI
Run REPL: python -m calculator.cli
Run tests: pytest --cov=calculator --cov-report=term --cov-fail-under=100

Calculator CLI:
A simple command-line calculator in Python supporting basic arithmetic operations and an interactive REPL. Designed for easy testing and full coverage with unit tests.

Features:
Basic arithmetic: +, -, *, /
Handles integers, floats, and scientific notation (e.g., 1e3)
Interactive REPL (Read-Eval-Print Loop)
Command-line arguments support for single operations
Comprehensive unit tests for all functions and CLI commands
100% test coverage

Installation Requirements:
Python 3.11+
pip

Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

Install the package and dependencies
pip install -e .
pip install pytest pytest-cov

Run the REPL
python -m calculator.cli

Example:
Enter operator (+, -, *, /) or 'exit': +
Enter first number: 2
Enter second number: 3
Result: 5

Type exit or quit to leave the REPL

Running Tests:
Run all tests and measure coverage:
pytest --maxfail=1 --disable-warnings -q --cov=calculator --cov-report=term --cov-fail-under=100
All tests should pass and coverage should be 100%.