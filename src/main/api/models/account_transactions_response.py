from __future__ import annotations
from typing import List, Optional
from src.main.api.models.base_model import BaseModel

class Transaction(BaseModel):
    transactionId: Optional[int] = None
    type: Optional[str] = None
    amount: Optional[float] = None
    fromAccountId: Optional[int] = None
    toAccountId: Optional[int] = None
    createdAt: Optional[str] = None

class AccountTransactionsResponse(BaseModel):
    id: Optional[int] = None
    number: Optional[str] = None
    balance: Optional[float] = None
    transactions: Optional[List[Transaction]] = None
    error: Optional[str] = None
