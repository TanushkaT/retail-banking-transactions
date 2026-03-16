from fastapi import FastAPI, UploadFile, File
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Retail Banking API is running!"}

@app.post("/ingest/")
async def ingest_data(file: UploadFile = File(...)):
    # 1. Read the uploaded JSON file
    content = await file.read()
    data = json.loads(content)
    
    # 2. Logic to loop through transactions
    # In a real app, you'd use 'psycopg2' here to send data to PostgreSQL
    batch_info = data.get("batch")
    records_count = len(data.get("transactions", []))
    
    return {
        "status": "Success",
        "batch_processed": batch_info,
        "total_records": records_count
    }
