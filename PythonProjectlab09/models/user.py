class User:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("id должен быть положительным целым числом")
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():  # strip(): xoa khoang trang thua
            raise ValueError("name должно быть непустой строкой")
        self.__name = value.strip()
