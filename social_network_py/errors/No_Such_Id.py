class NoSuchIdError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'NoSuchIdError: {self.mesaj}'
