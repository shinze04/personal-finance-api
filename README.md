# Personal Finance API

A simple personal finance management API built with FastAPI and PostgreSQL.

## Features
- Add a bill
- View all bills
- Delete a bill

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- psycopg2
- Render

## Live Demo
https://personal-finance-api-aehs.onrender.com/docs

## API Endpoints

### POST /bills
```json
{
  "type": "expense",
  "money": 20,
  "category": "food",
  "remark": "lunch"
}
```

### GET /bills

### DELETE /bills/{id}

## Setup

```
pip install -r requirements.txt
cd api-version
uvicorn main:app --reload
```

## Environment Variables

```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

## Database Schema

```sql
CREATE TABLE bills (
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL,
    money NUMERIC NOT NULL,
    category TEXT NOT NULL,
    remark TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```