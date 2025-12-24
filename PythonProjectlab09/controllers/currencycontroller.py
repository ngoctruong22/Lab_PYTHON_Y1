import sqlite3
from typing import List, Optional

from models.currency import Currency


class CurrencyCRUD:
    """CRUD operations for currencies table using parameterized SQL to avoid SQL injection."""

    def __init__(self, connection: Optional[sqlite3.Connection] = None):
        # Allow passing an existing connection for testing; otherwise use in-memory DB
        self._own_conn = connection is None
        self.con = sqlite3.connect(':memory:') if connection is None else connection
        # Return rows as tuples by default; we'll map manually
        self._create_table()

    def _create_table(self):
        # Schema follows the provided specification: table `currency`
        self.con.execute(
            "CREATE TABLE IF NOT EXISTS currency ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "num_code TEXT NOT NULL, "
            "char_code TEXT NOT NULL, "
            "name TEXT NOT NULL, "
            "value FLOAT, "
            "nominal INTEGER)"
        )
        self.con.commit()

    def create(self, num_code: str, char_code: str, name: str, value: float, nominal: int = 1) -> int:
        """Insert a new currency and return the new row id."""
        sql = "INSERT INTO currency (num_code, char_code, name, value, nominal) VALUES (?, ?, ?, ?, ?)"
        cur = self.con.cursor()
        cur.execute(sql, (num_code, char_code, name, float(value), int(nominal)))
        self.con.commit()
        return cur.lastrowid

    def list(self) -> List[dict]:
        sql = "SELECT id, num_code, char_code, name, value, nominal FROM currency ORDER BY id"
        cur = self.con.execute(sql)
        result = []
        for row in cur.fetchall():
            result.append({
                "id": int(row[0]),
                "num_code": row[1],
                "char_code": row[2],
                "name": row[3],
                "value": float(row[4]) if row[4] is not None else None,
                "nominal": int(row[5]) if row[5] is not None else None,
            })
        return result

    def get_by_id(self, currency_id: int) -> Optional[dict]:
        sql = "SELECT id, num_code, char_code, name, value, nominal FROM currency WHERE id = ?"
        cur = self.con.execute(sql, (int(currency_id),))
        row = cur.fetchone()
        if not row:
            return None
        return {
            "id": int(row[0]),
            "num_code": row[1],
            "char_code": row[2],
            "name": row[3],
            "value": float(row[4]) if row[4] is not None else None,
            "nominal": int(row[5]) if row[5] is not None else None,
        }

    def update_value_by_id(self, currency_id: int, new_value: float) -> int:
        """Update value for given id. Returns number of rows updated."""
        sql = "UPDATE currency SET value = ? WHERE id = ?"
        cur = self.con.cursor()
        cur.execute(sql, (float(new_value), int(currency_id)))
        self.con.commit()
        return cur.rowcount

    def delete_by_id(self, currency_id: int) -> int:
        """Delete currency by id. Returns number of rows deleted."""
        sql = "DELETE FROM currency WHERE id = ?"
        cur = self.con.cursor()
        cur.execute(sql, (int(currency_id),))
        self.con.commit()
        return cur.rowcount

    def __del__(self):
        try:
            if self._own_conn:
                self.con.close()
        except Exception:
            pass


class CurrencyController:
    """High-level controller that exposes CRUD operations to the rest of the app (MVC controller)."""

    def __init__(self, db: CurrencyCRUD):
        self.db = db

    def list_currencies(self):
        return self.db.list()

    def create_currency(self, num_code: str, char_code: str, name: str, value: float, nominal: int = 1):
        return self.db.create(num_code, char_code, name, value, nominal)

    def update_currency_value(self, currency_id: int, value: float):
        return self.db.update_value_by_id(currency_id, value)

    def delete_currency(self, currency_id: int):
        return self.db.delete_by_id(currency_id)
