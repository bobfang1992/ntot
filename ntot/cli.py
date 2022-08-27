import click

from ntot.notion import get_all_pages


@click.group()
@click.option("--dry-run", is_flag=True, help="Do not actually do anything")
def command_handler(dry_run):
    print("dry_run: {}".format(dry_run))


@command_handler.command()
@click.pass_context
def list_notion_pages(ctx):
    print("get_all_pages")
    print("result: {}".format(get_all_pages()))


if __name__ == "__main__":
    command_handler()
