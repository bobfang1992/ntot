import httpx

from ntot.notion.types import NotionPage


def get_default_auth_token():
    with open("./.notion-token") as f:
        return f.read().strip()


class NotionClient:
    def __init__(self, integration_token: str):
        self.integration_token = integration_token

    async def get_all_pages(self, async_client: httpx.AsyncClient):
        return await async_client.post(
            "https://api.notion.com/v1/search",
            headers={
                "Authorization": f"Bearer {self.integration_token}",
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28",
            },
        )

    async def enrich_page(self, async_client: httpx.AsyncClient, page_id: str, page: NotionPage):
        async def get_page_title():
            return await async_client.get(
                f"https://api.notion.com/v1/blocks/{page_id}",
                headers={
                    "Authorization": f"Bearer {self.integration_token}",
                    "Content-Type": "application/json",
                    "Notion-Version": "2022-06-28",
                },
            )
        page_data = (await get_page_title()).json()
        assert page_data["type"] == "child_page"
        page.title = page_data["child_page"]["title"]
        return page
