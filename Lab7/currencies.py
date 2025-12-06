import requests
import io
import sys
from Lab7.decorators import logger
from Lab7.logging_config import file_logger


# @logger(handle=sys.stdout)
# @logger(handle=io.StringIO)
# @logger(handle=file_logger)
@logger()
def get_currencies(currency_codes: list, url:str = "https://www.cbr-xml-daily.ru/daily_json.js")->dict:
    """
    Бизнес-логика: получает курсы валют.
    Исключения выбрасываются, логирование отсутствует.
    """
    #ket noi API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        currencies = {}
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as v_e:
            raise ValueError(f"Некорректный JSON: {v_e}")
        if "Valute" in data:
            for code in currency_codes:
                if code in data["Valute"]:
                    currencies[code] = data["Valute"][code]["Value"]
                else:
                    currencies[code] = f"Код валюты '{code}' не найден."
        else:
            raise KeyError("Нет ключа 'Valute'")
        return currencies
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"API недоступен: {e}\n")
    except KeyError as k_e:
        raise KeyError(f"Нет ключа “Valute”: {k_e}\n")
    except TypeError as t_e:
        raise TypeError(f"Курс валюты имеет неверный тип: {t_e}\n")


