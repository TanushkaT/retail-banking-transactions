from .database import engine, Base
from . import models

# This creates the tables in PostgreSQL if they don't exist
models.Base.metadata.create_all(bind=engine)

from fastapi import FastAPI, HTTPException
from .schemas import CustomerBatch  # Import your new validation rules

app = FastAPI()

@app.post("/upload-transactions/")
async def upload_json(data: CustomerBatch):
    # FastAPI automatically validates 'data' against CustomerBatch
    # If the JSON is wrong, it returns a clear error to the user
    return {
        "status": "Success",
        "message": f"Batch {data.batch_id} validated for Customer {data.customer_id}",
        "record_count": sum(len(acc.transactions) for acc in data.accounts)
    }
