from jinja2 import Environment, PackageLoader, select_autoescape
from models import *
from http.server import HTTPServer, BaseHTTPRequestHandler
from utils.currencies_api import get_currencies
from utils.get_currencies_history import get_currency_history
from urllib.parse import urlparse, parse_qs

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_currencies = env.get_template("currencies.html")
template_history = env.get_template("currency_history.html")
template_author = env.get_template("author.html")

main_author = Author('Ngoc Truong', 'P3124')
application = App(name="CurrenciesListApp", version="0.1", author=main_author)
users = [User(1, "Alice"), User(2, "Bob")]
user_currencies = [
    UserCurrency(1, 1, "USD"),
    UserCurrency(2, 1, "EUR"),
    # user_id 2 (Bob) theo dõi chỉ EUR
    UserCurrency(3, 2, "EUR")
]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if path == "/":
            result = self.index_page()
        elif path == "/author":
            result = self.author_page()
        elif path == "/users":
            result = self.page_users()
        elif path == "/currencies":
            result = self.page_currencies()
        elif path == "/user":
            # Lấy user_id từ query parameter
            user_id = query_params.get('id', [None])[0]
            if user_id:
                try:
                    user_id = int(user_id)
                    result = self.page_user_id(user_id)
                except (ValueError, IndexError):
                    result = "Invalid user ID"
            else:
                result = "User ID is required"
        elif path == "/currency":
            code = query_params.get("code", [None])[0]
            result = self.page_currency_history(code)
        else:
            result = "404 Page Not Found"

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes(result, 'utf-8'))

    def index_page(self):
        result = template_index.render(
            myapp=application.name,
            version=application.version,
            navigation=[{'caption': 'Основная страница', 'href': "/"}],
            author_name=main_author.name,
            group=main_author.group
        )
        return result

    def author_page(self):
        result = template_author.render(
            myapp=application.name,
            version=application.version,
            navigation=[{'caption': 'Основная страница', 'href': "/"}],
            author_name=main_author.name,
            group=main_author.group
        )
        return result

    def page_users(self):
        result = template_users.render(
            myapp=application.name,
            version=application.version,
            navigation=[{'caption': 'Основная страница', 'href': "/"}],
            users=users
        )
        return result
    def page_currencies(self):
        currencies_date, currencies_list = get_currencies()
        result = template_currencies.render(
            myapp=application.name,
            version=application.version,
            navigation=[{'caption': 'Основная страница', 'href': "/"}],
            currencies=currencies_list,
            currency_date= currencies_date
        )
        return result
    def page_user_id(self,user_id):

        user = None
        for u in users:
            if u.id == user_id:
                user = u
                break

        currency_date, currencies_list = get_currencies()

        currency_dict = {c.char_code: c for c in currencies_list}

        subs = [uc for uc in user_currencies if uc.user_id == user_id]

        subscriptions = []
        for s in subs:
            if s.currency_id in currency_dict:
                subscriptions.append(currency_dict[s.currency_id])

        result = template_users.render(
            myapp=application.name,
            version=application.version,
            navigation=[{'caption': 'список пользователей', 'href': "/users"}],
            users=None,
            user=user,
            subscriptions=subscriptions
        )
        return result

    def page_currency_history(self, code):
        if not code:
            return "Currency code required"

        history = get_currency_history(code)

        labels = ",".join([f'"{h["date"]}"' for h in history])

        values = ",".join([str(h["value"]) for h in history])

        result = template_history.render(
            code=code,
            labels=labels,
            values=values
        )
        return result






httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print('server is running')
httpd.serve_forever()