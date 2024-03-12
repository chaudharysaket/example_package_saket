import click

@click.command()
@click.option('--name', default='World', help='Name to greet.')
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f'Hello {name}!')
