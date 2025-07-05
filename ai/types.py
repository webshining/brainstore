from datetime import datetime as dt
from enum import Enum
from typing import Generic, TypeVar, Optional

from pydantic import BaseModel, Field

T = TypeVar("T")


class AICategory(Enum):
    REMINDER = "reminder"
    NOTES = "notes"


class AIResponse(BaseModel, Generic[T]):
    prompt: str
    request: str | None = None
    response: T


class AIReminder(BaseModel):
    title: str
    message: str
    is_once: bool
    posix_cron: Optional[str] = Field(None, description="Required if is_once is False")
    datetime: Optional[dt] = Field(None, description="Required if is_once is True")
