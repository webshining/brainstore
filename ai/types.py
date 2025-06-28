from datetime import datetime
from typing import List

from pydantic import BaseModel


class ReminderItem(BaseModel):
    title: str
    task: str
    is_once: bool
    cron: str | None
    datetime: datetime | None


class ReminderResponse(BaseModel):
    reminders: List[ReminderItem]
