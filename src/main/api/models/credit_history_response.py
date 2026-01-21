from __future__ import annotations
from typing import List, Optional
from src.main.api.models.base_model import BaseModel

class CreditItem(BaseModel):
    creditId: Optional[int] = None
    accountId: Optional[int] = None
    amount: Optional[float] = None
    termMonths: Optional[int] = None
    balance: Optional[float] = None
    createdAt: Optional[str] = None

class CreditHistoryResponse(BaseModel):
    userId: Optional[int] = None
    credits: Optional[List[CreditItem]] = None
    error: Optional[str] = None
