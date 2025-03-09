from enum import Enum, auto


class GameState(Enum):
    INIT = auto()
    PLAYER_TURN = auto()
    CHECK_WIN = auto()
    GAME_OVER = auto()


class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.turn = 0
        self.state = GameState.INIT

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("---------")

    def check_winner(self, player):
        """Checks if the given player has won."""
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
                    all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
                all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] in ['X', 'O'] for i in range(3) for j in range(3))

    def player_turn(self):
        """Handles player move input."""
        self.print_board()
        player = self.players[self.turn % 2]
        print(f"Player {player}'s turn")
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if self.board[row][col] == " ":
                    self.board[row][col] = player
                    break
                else:
                    print("Cell is already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter numbers between 0 and 2.")
        self.state = GameState.CHECK_WIN

    def check_game_status(self):
        """Checks if there is a winner or if the game is a draw."""
        player = self.players[self.turn % 2]
        if self.check_winner(player):
            self.print_board()
            print(f"Player {player} wins!")
            self.state = GameState.GAME_OVER
        elif self.is_draw():
            self.print_board()
            print("It's a draw!")
            self.state = GameState.GAME_OVER
        else:
            self.turn += 1
            self.state = GameState.PLAYER_TURN

    def run(self):
        """Main game loop."""
        self.state = GameState.PLAYER_TURN
        while self.state != GameState.GAME_OVER:
            if self.state == GameState.PLAYER_TURN:
                self.player_turn()
            elif self.state == GameState.CHECK_WIN:
                self.check_game_status()


# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
