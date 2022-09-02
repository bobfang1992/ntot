import asyncio

import click
import httpx

from ntot.notion import (NotionClient, get_default_auth_token,
                         pretty_print_pages)


@click.group()
@click.option("--dry-run", is_flag=True, help="Do not actually do anything")
def command_handler(dry_run):
    print("dry_run: {}".format(dry_run))


@command_handler.command()
def print_all_pages():
    print("print_all_pages")

    async def run():
        async with httpx.AsyncClient() as client:
            notion = NotionClient(get_default_auth_token())
            pages = await notion.get_all_pages(client)
            pretty_print_pages(pages)

    asyncio.run(run())


if __name__ == "__main__":
    command_handler()
