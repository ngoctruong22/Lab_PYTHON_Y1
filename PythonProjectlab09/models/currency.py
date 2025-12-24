class Currency:
    def __init__(self, id: str, num_code: str, char_code: str, name: str, value: float, nominal: int = 1):
        self.__id = id
        self.__num_code = num_code
        self.__char_code = char_code
        self.__name = name
        self.__value = value
        self.__nominal = nominal

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("id должно быть непустой string")
        self.__id = value

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("num_code должно быть string")
        self.__num_code = value

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("char_code должно быть непустой string")
        self.__char_code = value.upper()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("name должно быть string")
        self.__name = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            value = float(value)
        except Exception:
            raise ValueError("value должно быть float")
        self.__value = value

    @property
    def nominal(self):
        return self.__nominal

    @nominal.setter
    def nominal(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("nominal должен быть положительным целым числом")
        self.__nominal = value