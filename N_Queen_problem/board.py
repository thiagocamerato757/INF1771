from queen import Queen
class Board:
    __width: int
    __height: int
    __queens: list[tuple]
    __board: list[list[Queen]]

    def __init__(self, num: int) -> None:
        self.__width = num
        self.__height = num
        self.__queens = []
        self.__board = []
        for i in range(num):
            row = []
            for j in range(num):
                row.append(Queen())
            self.__board.append(row)

    def is_safe(self, row: int, col: int) -> bool:
        """
        Check if the given row and column are safe to place a queen.

        Parameters:
            row (int): The row index of the queen.
            col (int): The column index of the queen.

        Returns:
            bool: `True` if the given row and column are safe to place a queen;
                  `False` otherwise.
        """
        # check column
        for i in range(col):
            if self.__board[row][i].get_placed():
                return False

        # check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.__board[i][j].get_placed():
                return False

        # check upper right diagonal
        for i, j in zip(range(row, self.__height), range(col, -1, -1)):
            if self.__board[i][j].get_placed():
                return False

        return True

    def solve_n_queens(self, col: int = 0) -> bool:
        """
        Recursive function to solve the N-Queens problem.

        Parameters:
            col (int): The current column index.

        Returns:
            bool: `True` if a valid placement of queens is found; `False` otherwise.

        This function uses backtracking to place queens on the board in a way that
        no two queens can attack each other. It starts by trying all possible
        rows in the current column, and recursively calls itself with the next
        column. If a valid placement is found, it returns `True`. If all rows
        in the current column have been tried and no valid placement found,
        it backtracks and returns `False`.
        """
        if col >= self.__width:
            return True

        for i in range(self.__height):
            if self.is_safe(i, col):
                self.__board[i][col].set_placed(True)
                self.__queens.append((i, col))

                if self.solve_n_queens(col + 1):
                    return True

                # Backtrack
                self.__board[i][col].set_placed(False)
                self.__queens.pop()

        return False

    def show_board(self) -> None:
        print(self.__queens)
        print()
        for i in range(self.__width):
            for j in range(self.__height):
                print(self.__board[i][j], end=" | ")
            print()


if __name__ == "__main__":
    board = Board(8)
    if board.solve_n_queens():
        board.show_board()
    else:
        print("No solution found.")