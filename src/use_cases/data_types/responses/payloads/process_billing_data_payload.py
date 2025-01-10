from typing import Optional

from pydantic import BaseModel


class ProcessBillingDataPayload(BaseModel):
    total: Optional[int] = None
