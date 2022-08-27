from datetime import datetime

from pydantic import BaseModel


class ParentPage(BaseModel):
    type: str
    page_id: str


class NotionPage(BaseModel):
    id: str
    created_time: datetime
    last_edited_time: datetime
    parent: ParentPage
