import sqlite3


class CurrencyRatesCRUD():
    def __init__(self, currency_rates_obj):
        self.__con = sqlite3.connect(':memory:')
        self.__createtable()
        self.__cursor = self.__con.cursor()
        self.__currency_rates_obj = currency_rates_obj

    def __createtable(self):
        self.__con.execute(
            "CREATE TABLE IF NOT EXISTS currency("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "cur TEXT,"
            "date TEXT DEFAULT CURRENT_TIMESTAMP,"
            "value FLOAT);")
        self.__con.commit()

    def _create(self):
        __params = self.__currency_rates_obj.values
        # [("USD", "02-04-2025 11:10", "90"), ("EUR", "02-04-2025 11:11", "91")]
        __sqlquery = "INSERT INTO currency(cur,  value) VALUES(?, ?)"

        # TODO: реализовать именованный стиль запроса
        # This is the named style used with executemany():
        # data = (
        #     {"name": "C", "year": 1972},
        #     {"name": "Fortran", "year": 1957},
        #     {"name": "Python", "year": 1991},
        #     {"name": "Go", "year": 2009},
        # )
        # cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

        self.__cursor.executemany(__sqlquery, __params)
        self.__con.commit()

    def _read(self):
        # TODO: Реализовать параметризованный запрос на получение значения валют по коду: строка из трех символов
        cur = self.__con.execute("SELECT * FROM currency")
        # result_data = list(zip(['id', 'cur', 'date', 'value'], cur))
        result_data = []
        for _row in cur:
            _d = {'id': int(_row[0]), 'cur': _row[1], 'date': _row[2], 'value': float(_row[3])}
            result_data.append(_d)

        return result_data

    def _delete(self, currency_id):
        del_statement = "DELETE FROM currency WHERE id = " + str(currency_id)
        print(del_statement)
        self.__cursor.execute(del_statement)
        self.__con.commit()

        pass

    def _update(self, currency: dict['str': float]):
        # ...._update({'USD': 101.1})
        currency_code = tuple(currency.keys())[0]
        currency_value = tuple(currency.values())[0]
        upd_statement = f"UPDATE currency SET value = {currency_value} WHERE cur = '" + str(currency_code) + "'"
        print(upd_statement)
        self.__cursor.execute(upd_statement)
        self.__con.commit()

    def __del__(self):
        self.__cursor = None
        self.__con.close()