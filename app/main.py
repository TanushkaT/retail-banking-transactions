from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import SessionLocal, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload-transactions/")
def upload_json(data: schemas.CustomerBatch, db: Session = Depends(get_db)):
    try:
        batch_id = crud.ingest_transaction_data(db, data)
        return {"status": "Success", "batch_processed": batch_id}
    except Exception as e:
        db.rollback() # Rollback if something goes wrong
        raise HTTPException(status_code=400, detail=str(e))
