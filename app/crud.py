from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def ingest_transaction_data(db: Session, data: schemas.CustomerBatch):
    # 1. Create a Batch record
    db_batch = models.Batch(
        batch_id=data.batch_id, 
        uploaded_at=datetime.utcnow()
    )
    db.add(db_batch)

    # 2. Check/Create Customer (Use 'merge' to avoid duplicates)
    db_customer = models.Customer(customer_id=data.customer_id)
    db.merge(db_customer)

    # 3. Process Accounts and Transactions
    for acc in data.accounts:
        db_account = models.Account(
            account_id=acc.account_id,
            customer_id=data.customer_id,
            balance=acc.balance
        )
        db.merge(db_account) # Updates balance if account exists

        for txn in acc.transactions:
            db_txn = models.Transaction(
                transaction_id=txn.transaction_id,
                account_id=acc.account_id,
                batch_id=data.batch_id,
                amount=txn.amount,
                merchant=txn.merchant,
                type=txn.type,
                date=txn.date
            )
            db.add(db_txn)

    # 4. Commit everything as ONE atomic transaction
    # If any line above fails, nothing is saved to the DB
    db.commit()
    return data.batch_id
