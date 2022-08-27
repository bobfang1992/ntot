import httpx


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
