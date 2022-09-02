from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel


class RawParentPageMetadata(BaseModel):
    type: str
    page_id: Optional[str]


class RawNotionPageMetadata(BaseModel):
    id: str
    created_time: datetime
    last_edited_time: datetime
    object: Literal["page", "database"]
    parent: RawParentPageMetadata
    url: str
