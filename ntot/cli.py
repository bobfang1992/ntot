from venv import EnvBuilder
import click

from ntot.notion import get_all_pages, pretty_print_pages, enrich_page


@click.group()
@click.option("--dry-run", is_flag=True, help="Do not actually do anything")
def command_handler(dry_run):
    print("dry_run: {}".format(dry_run))


@command_handler.command()
@click.pass_context
def list_notion_pages(ctx):
    print("get_all_pages")
    print(pretty_print_pages(get_all_pages()))


@command_handler.command()
@click.pass_context
@click.option("--page-id", "-p", help="Page id", required=True)
def get_page_content(ctx, page_id):
    print("get_page_content")
    result = enrich_page(page_id)
    print(result)


if __name__ == "__main__":
    command_handler()
