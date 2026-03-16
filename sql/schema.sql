CREATE TABLE batches (
    batch_id VARCHAR(50) PRIMARY KEY, -- e.g., BATCH_008
    total_records INT,
    generated_at TIMESTAMP
);

CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY, -- e.g., CIF48561759
    name VARCHAR(100),
    email VARCHAR(100),
    pan_number VARCHAR(20)
);

CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY, -- e.g., TXNCF0CCD6D5D734208
    batch_id VARCHAR(50) REFERENCES batches(batch_id),
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    amount DECIMAL(18, 2),
    currency VARCHAR(10),
    transaction_date DATE
);
