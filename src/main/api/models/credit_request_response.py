from typing import Optional
from src.main.api.models.base_model import BaseModel

class CreditRequestResponse(BaseModel):
    accountId: Optional[int] = None
    amount: Optional[float] = None
    termMonths: Optional[int] = None
    balance: Optional[float] = None
    creditId: Optional[int] = None
    error: Optional[str] = None
