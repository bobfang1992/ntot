from typing import List

from ntot.notion.types import NotionPage


def json_to_page(json_data: dict) -> List[NotionPage]:
    result = []
    for page in json_data["results"]:
        # breakpoint()
        result.append(NotionPage(**page))
    return result
