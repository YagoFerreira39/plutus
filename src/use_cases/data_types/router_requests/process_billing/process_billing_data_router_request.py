from dataclasses import dataclass
from fastapi import UploadFile, File

dataclass(slots=True)


class ProcessBillingDataRouterRequest:
    file: UploadFile = File(...)
