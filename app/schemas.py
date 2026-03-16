from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class TransactionBase(BaseModel):
    transaction_id: str
    amount: float = Field(..., gt=0)  # Must be greater than 0
    date: datetime
    merchant: str
    type: str

class AccountBase(BaseModel):
    account_id: str
    balance: float
    transactions: List[TransactionBase]

class CustomerBatch(BaseModel):
    batch_id: str
    customer_id: str
    accounts: List[AccountBase]
