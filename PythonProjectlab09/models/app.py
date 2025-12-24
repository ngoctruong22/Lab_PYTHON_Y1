class App:
    def __init__(self, name: str, version: str, author: str):
        self.name = name
        self.version = version
        self.author = author

    def to_dict(self):
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author
        }