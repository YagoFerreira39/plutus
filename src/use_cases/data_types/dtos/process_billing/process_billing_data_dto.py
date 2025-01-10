from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ProcessBillingDataDto:
    total: int = None
