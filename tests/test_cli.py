from calculator import cli

def test_cli_dunder_main_coverage():
    """Cover the if __name__ == '__main__' block in cli.py."""
    inputs = iter(['+', '1', '2', 'quit'])
    outputs = []

    def fake_input(prompt=''):
        return next(inputs)

    def fake_print(*args):
        outputs.append(' '.join(map(str, args)))

    # Call the entry point explicitly
    cli._cli_main_wrapper(input_func=fake_input, output_func=fake_print)

    assert any("Result: 3.0" in line for line in outputs)
