from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class RequestCategory(Enum):
    NOTES = "notes"
    REMINDERS = "reminders"


class RequestCategoryResponse(BaseModel):
    category: RequestCategory


class ReminderItem(BaseModel):
    title: str
    task: str
    is_once: bool
    cron: str | None
    datetime: datetime | None


class ReminderResponse(BaseModel):
    reminders: List[ReminderItem]
