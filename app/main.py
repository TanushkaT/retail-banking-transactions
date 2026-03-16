from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import SessionLocal, engine
from typing import List

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


@app.post("/upload-transactions-bulk/")
def upload_multiple_jsons(batches: List[schemas.CustomerBatch], db: Session = Depends(get_db)):
    processed_ids = []
    for batch_data in batches:
        batch_id = crud.ingest_transaction_data(db, batch_data)
        processed_ids.append(batch_id)
    return {"status": "Success", "processed_batches": processed_ids}

@app.post("/upload-transactions/")
def upload_json(data: schemas.CustomerBatch, db: Session = Depends(get_db)):
    try:
        batch_id = crud.ingest_transaction_data(db, data)
        return {"status": "Success", "batch_processed": batch_id}
    except Exception as e:
        db.rollback() # Rollback if something goes wrong
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/summaries/file/{batch_id}")
def read_file_summary(batch_id: str, db: Session = Depends(get_db)):
    summary = crud.get_file_summary(db, batch_id)
    if not summary:
        raise HTTPException(status_code=404, detail="Batch not found")
    return summary

@app.get("/summaries/overall")
def read_overall_summary(db: Session = Depends(get_db)):
    return crud.get_overall_summary(db)
