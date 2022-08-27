import asyncio

import httpx

from ntot.notion.client import NotionClient, get_default_auth_token
from ntot.notion.utils import json_to_page


async def async_get_all_pages(notion_client: NotionClient) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        r = notion_client.get_all_pages(client)
        return await r


def get_all_pages():
    notion_client = NotionClient(integration_token=get_default_auth_token())
    result = asyncio.run(async_get_all_pages(notion_client))
    pages = json_to_page(result.json())
    return pages
