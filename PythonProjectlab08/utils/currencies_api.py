import requests
from PythonProjectlab08.models.currency import Currency


def get_currencies(url: str = "https://www.cbr-xml-daily.ru/daily_json.js"):
    """
    Бизнес-логика: получает курсы валют.
    Исключения выбрасываются, логирование отсутствует.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        currencies = []
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as v_e:
            raise ValueError(f"Некорректный JSON: {v_e}")
        if "Valute" in data:
            currencies_valute = data["Valute"]
            currencies_date = data.get("Date","")
            # Lặp qua từng currency trong Valute
            for currency_code, currency_data in currencies_valute.items():
                currencies_id = currency_data["ID"]
                currencies_num_code = currency_data["NumCode"]
                currencies_char_code = currency_data["CharCode"]
                currencies_name = currency_data["Name"]
                currencies_value = currency_data["Value"]
                currencies_nominal = currency_data["Nominal"]
                cur = Currency(currencies_id, currencies_num_code, currencies_char_code,
                             currencies_name, currencies_value, currencies_nominal)
                currencies.append(cur)
        else:
            raise KeyError("Нет ключа 'Valute'")
        return currencies_date,currencies
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"API недоступен: {e}\n")
    except KeyError as k_e:
        raise KeyError(f"Нет ключа “Valute”: {k_e}\n")
    except TypeError as t_e:
        raise TypeError(f"Курс валюты имеет неверный тип: {t_e}\n")

