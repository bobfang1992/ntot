import asyncio

import httpx

from ntot.notion.types import NotionPage
from ntot.notion.client import NotionClient, get_default_auth_token
from ntot.notion.utils import json_to_page, pretty_print_pages  # noqa: F401


async def async_get_all_pages(notion_client: NotionClient) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        r = notion_client.get_all_pages(client)
        return await r


async def async_enrich_page(notion_client: NotionClient, page_id: str, page: NotionPage):
    async with httpx.AsyncClient() as client:
        r = notion_client.enrich_page(client, page_id, page)
        return await r


async def async_enrich_all_pages(notion_client: NotionClient):
    async with httpx.AsyncClient() as client:
        pages = await async_get_all_pages(notion_client)
        pages = json_to_page(pages.json())
        await asyncio.gather(*[notion_client.enrich_page(
            client, page.id, page) for page in pages])
        return pages


def get_all_pages():
    notion_client = NotionClient(integration_token=get_default_auth_token())
    result = asyncio.run(async_get_all_pages(notion_client))
    pages = json_to_page(result.json())
    return pages


def enrich_page(page_id: str):
    page = NotionPage(id=page_id,
                      created_time=None,
                      last_edited_time=None,
                      parent=None,
                      url=None,
                      title=None)
    notion_client = NotionClient(integration_token=get_default_auth_token())
    asyncio.run(async_enrich_page(notion_client, page_id, page))
    return page


def enrich_all_pages():
    notion_client = NotionClient(integration_token=get_default_auth_token())
    pages = asyncio.run(async_enrich_all_pages(notion_client))
    return pages


if __name__ == '__main__':
    result = enrich_all_pages()
    print(pretty_print_pages(result))
