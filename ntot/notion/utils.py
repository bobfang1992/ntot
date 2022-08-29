from typing import List

from ntot.notion.types import NotionPage


def json_to_page(json_data: dict) -> List[NotionPage]:
    result = []
    for page in json_data["results"]:
        # breakpoint()
        result.append(NotionPage(**page))
    return result


def pretty_print_pages(pages: List[NotionPage]) -> str:
    result = ""
    for page in pages:
        result += f"""id: {page.id} {page.created_time} {page.last_edited_time} parent:{page.parent.page_id}
title:{page.title}\n"""
    return result
