🏦 Retail Banking Transaction Pipeline
An Industrial-Grade Data Engineering & Analytics Workflow
📌 Project Overview
This project demonstrates an end-to-end data pipeline that ingests hierarchical banking JSON files, validates them using Pydantic, stores them in a normalized PostgreSQL database, and visualizes transaction summaries through an interactive dashboard.
🏗️ System Architecture
Ingestion Layer: FastAPI endpoint receiving JSON batches.
Validation Layer: Pydantic models ensuring data types, mandatory fields, and positive currency values.
Database Layer: PostgreSQL with a 3NF normalized schema (Batches, Customers, Accounts, Transactions).
Processing Layer: SQLAlchemy-based CRUD logic with atomic transaction handling.
Presentation Layer: Vanilla JS + Chart.js dashboard for real-time business insights.
🛠️ Tech Stack
Backend: Python, FastAPI
Database: PostgreSQL, SQLAlchemy (ORM)
Validation: Pydantic
Frontend: HTML5, CSS3, JavaScript, Chart.js
Environment: Docker (Optional), Uvicorn
📊 Database Schema (Normalized)
Batches: batch_id (PK), uploaded_at
Customers: customer_id (PK), name
Accounts: account_id (PK), customer_id (FK), balance
Transactions: transaction_id (PK), account_id (FK), batch_id (FK), amount, merchant, date
🚀 Getting Started
1. Prerequisites
Python 3.9+
PostgreSQL installed and running
