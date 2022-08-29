from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ParentPage(BaseModel):
    type: str
    page_id: str


class NotionPage(BaseModel):
    id: str
    created_time: Optional[datetime]
    last_edited_time: Optional[datetime]
    parent: Optional[ParentPage]
    url: Optional[str]
    title: Optional[str]
