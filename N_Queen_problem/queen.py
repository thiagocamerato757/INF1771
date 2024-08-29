class Queen:
    __position: tuple
    __placed: bool

    def __init__(self) -> None:
        self.__placed = False

    def __str__(self) -> str:
        return "♛" if self.__placed else "·"

    def set_placed(self, boolean: bool) -> None:
        self.__placed = boolean

    def get_placed(self) -> bool:
        return self.__placed

    def set_position(self, position: tuple) -> None:
        self.__position = position

    def get_position(self) -> tuple:
        return self.__position