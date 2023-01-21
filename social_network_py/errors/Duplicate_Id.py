
class DuplicateIdError(Exception):
    mesaj: any

    def __str__(self) -> str:
        return f'DuplicateIdError: {self.mesaj}'
