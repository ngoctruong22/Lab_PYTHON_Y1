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

        # TODO ĐÃ HOÀN THÀNH: thực hiện named style query với executemany
        __sqlquery = "INSERT INTO currency(cur, value) VALUES(:cur, :value)"

        # Chuyển đổi dữ liệu từ tuple sang dictionary với named parameters
        named_params = []
        for param in __params:
            # param có dạng: ("USD", "90") hoặc ("USD", "02-04-2025 11:10", "90")
            # Chỉ lấy currency code và value, bỏ qua date nếu có
            named_params.append({"cur": param[0], "value": float(param[-1])})

        self.__cursor.executemany(__sqlquery, named_params)
        self.__con.commit()

    def _read(self, currency_code=0):
        # TODO ĐÃ HOÀN THÀNH: thực hiện parameterized query để lấy giá trị theo mã tiền tệ
        if currency_code:
            # Sử dụng parameterized query để tránh SQL injection
            # Lọc theo mã tiền tệ (3 ký tự)
            sql_query = "SELECT * FROM currency WHERE cur = ?"
            cur = self.__con.execute(sql_query, (currency_code,))
        else:
            # Nếu không có mã tiền tệ, lấy tất cả
            cur = self.__con.execute("SELECT * FROM currency")

        result_data = []
        for _row in cur:
            _d = {'id': int(_row[0]), 'cur': _row[1], 'date': _row[2], 'value': float(_row[3])}
            result_data.append(_d)

        return result_data

    def _delete(self, currency_id):
        # Use parameterized query to avoid SQL injection
        del_statement = "DELETE FROM currency WHERE id = ?"
        self.__cursor.execute(del_statement, (int(currency_id),))
        self.__con.commit()

    def _update(self, currency: dict['str': float]):
        # ...._update({'USD': 101.1})
        currency_code = tuple(currency.keys())[0]
        currency_value = tuple(currency.values())[0]
        # Use parameterized query to avoid SQL injection and validate value
        try:
            currency_value = float(currency_value)
        except Exception:
            raise ValueError("value должен быть числом")

        upd_statement = "UPDATE currency SET value = ? WHERE cur = ?"
        self.__cursor.execute(upd_statement, (currency_value, str(currency_code)))
        self.__con.commit()

    def __del__(self):
        self.__cursor = None
        self.__con.close()