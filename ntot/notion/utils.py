from typing import List

from loguru import logger

from ntot.notion.types import RawNotionPageMetadata


def pretty_print_pages(pages: List[RawNotionPageMetadata]):
    for p in pages:
        logger.info(f"{p.id} {p.object} {p.url}")
