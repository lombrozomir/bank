from typing import Optional
from src.main.api.models.base_model import BaseModel

class CreditRepayResponse(BaseModel):
    creditId: Optional[int] = None
    amountDeposited: Optional[float] = None
    error: Optional[str] = None
