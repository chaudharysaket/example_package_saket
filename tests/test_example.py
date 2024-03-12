import click
from click.testing import CliRunner
import pytest

# Assuming your Click command is in a file named 'your_script.py'
from example_package_saketc import hello

def test_hello_default():
    """Test the hello function with default name."""
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert "Hello World!" in result.output

def test_hello_with_name():
    """Test the hello function with a provided name."""
    runner = CliRunner()
    result = runner.invoke(hello, ['--name', 'Alice'])
    assert result.exit_code == 0
    assert "Hello Alice!" in result.output
