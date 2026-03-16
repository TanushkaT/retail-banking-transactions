from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Batch(Base):
    __tablename__ = "batches"
    batch_id = Column(String, primary_key=True)
    uploaded_at = Column(DateTime)

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(String, primary_key=True)
    name = Column(String)

class Account(Base):
    __tablename__ = "accounts"
    account_id = Column(String, primary_key=True)
    customer_id = Column(String, ForeignKey("customers.customer_id"))
    balance = Column(Float)

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(String, primary_key=True)
    account_id = Column(String, ForeignKey("accounts.account_id"))
    batch_id = Column(String, ForeignKey("batches.batch_id"))
    amount = Column(Float)
    merchant = Column(String)
    type = Column(String)
    date = Column(DateTime)
