import requests
from datetime import datetime, timedelta

def get_currency_history(char_code: str, days: int = 90):
    results = []
    today = datetime.now()

    for i in range(days):
        day = today - timedelta(days=i)
        url = f"https://www.cbr-xml-daily.ru/archive/{day:%Y/%m/%d}/daily_json.js"

        try:
            res = requests.get(url, timeout=3)
            if res.status_code != 200:
                continue

            data = res.json()
            val = data.get("Valute", {})

            if char_code not in val:
                continue

            rate = val[char_code]["Value"]

            results.append({
                "date": day.strftime("%Y-%m-%d"),
                "value": rate
            })
        except:
            continue

    results.reverse()
    return results
