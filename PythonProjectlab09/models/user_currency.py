class UserCurrency:
    def __init__(self, id: int, user_id: int, currency_id: str):
        self.__id = id
        self.__user_id = user_id
        self.__currency_id = currency_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, v: int):
        if not isinstance(v, int) or v <= 0:
            raise ValueError("id должен быть положительным целым числом")
        self.__id = v

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, v: int):
        if not isinstance(v, int) or v <= 0:
            raise ValueError("user_id должен быть положительным целым числом")
        self.__user_id = v

    @property
    def currency_id(self):
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, v: str):
        if not isinstance(v, str) or not v:
            raise ValueError("currency_id должно быть непустой string")
        self.__currency_id = v