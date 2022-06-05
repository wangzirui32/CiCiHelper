import click
from .read_cmd import ReadCmd

@click.group()
def cli(): pass

@click.command()
@click.option('--name', help='需要查询的命令名称')
def query_name(name):
    table = ReadCmd.show_cmds(ReadCmd.query_cmd_name(name))
    click.echo(table)

@click.command()
@click.option('--desc', help='需要查询的命令关键词')
def query_desc(desc):
    table = ReadCmd.show_cmds(ReadCmd.query_cmd_desc(desc))
    click.echo(table)

cli.add_command(query_name)
cli.add_command(query_desc)

if __name__ == '__main__':
    cli()