from dataclasses import dataclass

from fastapi import UploadFile


@dataclass(slots=True)
class ProcessBillingDataRequest:
    file: UploadFile
