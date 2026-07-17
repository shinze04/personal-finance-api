from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_connection

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Bill(BaseModel):
    type: str
    money: float
    category: str
    remark: str


@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/bills")
def add_bill(bill: Bill):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO bills (type, money, category, remark)
        VALUES (%s, %s, %s, %s)
        """,
        (bill.type, bill.money, bill.category, bill.remark)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Bill added successfully"}


@app.get("/bills")
def get_bills():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, type, money, category, remark, created_at FROM bills"
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    bills = []

    for row in rows:
        bills.append({
            "id": row[0],
            "type": row[1],
            "money": float(row[2]),
            "category": row[3],
            "remark": row[4],
            "created_at": str(row[5])
        })

    return bills

@app.delete("/bills/{bill_id}")
def delete_bill(bill_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM bills WHERE id = %s",
        (bill_id,)
    )

    conn.commit()

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        return {"error": "Bill not found"}

    cur.close()
    conn.close()

    return {"message": "Bill deleted successfully"}