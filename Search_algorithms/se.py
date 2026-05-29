import random
import math

# ==========================================
# TIC TAC TOE BOARD
# ==========================================
class TicTacToe:
    def __init__(self, board=None, player="X"):
        if board:
            self.board = board[:]
        else:
            self.board = [" "] * 9

        self.player = player

    def display(self):

        print()
        for i in range(0, 9, 3):
            print(
                self.board[i],
                "|",
                self.board[i + 1],
                "|",
                self.board[i + 2]
            )

            if i < 6:
                print("---------")
        print()

    def legal_moves(self):
        return [
            i
            for i in range(9)
            if self.board[i] == " "
        ]
    def make_move(self, move):
        new_board = self.board[:]
        new_board[move] = self.player
        next_player = (
            "O"
            if self.player == "X"
            else "X"
        )

        return TicTacToe(
            new_board,
            next_player
        )
    def winner(self):

        wins = [
            (0,1,2),
            (3,4,5),
            (6,7,8),

            (0,3,6),
            (1,4,7),
            (2,5,8),

            (0,4,8),
            (2,4,6)
        ]

        for a,b,c in wins:

            if (
                self.board[a]
                ==
                self.board[b]
                ==
                self.board[c]
                != " "
            ):

                return self.board[a]
        return None
    def is_terminal(self):

        if self.winner():
            return True
        return " " not in self.board

    def utility(self):
        w = self.winner()
        if w == "X":
            return 1

        if w == "O":
            return -1
        return 0

    def heuristic(self):
        score = 0
        lines = [

            (0,1,2),
            (3,4,5),
            (6,7,8),

            (0,3,6),
            (1,4,7),
            (2,5,8),

            (0,4,8),
            (2,4,6)
        ]

        for a,b,c in lines:

            values = [
                self.board[a],
                self.board[b],
                self.board[c]
            ]
            if values.count("X") == 2 \
                    and values.count(" ") == 1:
                score += 10

            if values.count("O") == 2 \
                    and values.count(" ") == 1:
                score -= 10
        return score
      
  # ==========================================
# MINIMAX
# ==========================================
def minimax(state):
    def max_value(s):
        if s.is_terminal():
            return s.utility(), None
        best_score = -math.inf
        best_move = None
        for move in s.legal_moves():

            score, _ = min_value(
                s.make_move(move)
            )
            if score > best_score:

                best_score = score
                best_move = move

        return best_score, best_move
    def min_value(s):

        if s.is_terminal():
            return s.utility(), None
        best_score = math.inf
        best_move = None

        for move in s.legal_moves():

            score, _ = max_value(
                s.make_move(move)
            )
            if score < best_score:

                best_score = score
                best_move = move
        return best_score, best_move

    if state.player == "X":
        return max_value(state)

    return min_value(state)
 
 # ==========================================
# ALPHA BETA
# ==========================================
def alpha_beta_search(state):

    def max_value(s, alpha, beta):
        if s.is_terminal():
            return s.utility(), None
        best_score = -math.inf
        best_move = None
        for move in s.legal_moves():
            score, _ = min_value(
                s.make_move(move),
                alpha,
                beta
            )
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score, best_move
    def min_value(s, alpha, beta):
        if s.is_terminal():
            return s.utility(), None
        best_score = math.inf
        best_move = None
        for move in s.legal_moves():

            score, _ = max_value(
                s.make_move(move),
                alpha,
                beta
            )
            if score < best_score:

                best_score = score
                best_move = move

            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_score, best_move
    if state.player == "X":
        return max_value(
            state,
            -math.inf,
            math.inf
        )
    return min_value(
        state,
        -math.inf,
        math.inf
    )
    
# ==========================================
# HEURISTIC ALPHA BETA
# ==========================================

def heuristic_alpha_beta(
    state,
    depth_limit
):
    def max_value(
        s,
        alpha,
        beta,
        depth
    ):
        if s.is_terminal():
            return s.utility(), None
        if depth == 0:
            return s.heuristic(), None
        best_score = -math.inf
        best_move = None

        for move in s.legal_moves():
            score, _ = min_value(
                s.make_move(move),
                alpha,
                beta,
                depth - 1
            )
            if score > best_score:

                best_score = score
                best_move = move
            alpha = max(
                alpha,
                best_score
            )

            if alpha >= beta:
                break
        return best_score, best_move
    def min_value(
        s,
        alpha,
        beta,
        depth
    ):
        if s.is_terminal():
            return s.utility(), None
        if depth == 0:
            return s.heuristic(), None
        best_score = math.inf
        best_move = None
        for move in s.legal_moves():
            score, _ = max_value(
                s.make_move(move),
                alpha,
                beta,
                depth - 1
            )
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(
                beta,
                best_score
            )
            if alpha >= beta:
                break
        return best_score, best_move
    if state.player == "X":
        return max_value(
            state,
            -math.inf,
            math.inf,
            depth_limit
        )

    return min_value(
        state,
        -math.inf,
        math.inf,
        depth_limit
    )
# ==========================================
# MONTE CARLO TREE SEARCH
# ==========================================
class MonteCarloTreeSearch:
    def __init__(
        self,
        iterations=1000
    ):
        self.iterations = iterations
    def search(
        self,
        initial_state
    ):
        move_scores = {}
        for move in initial_state.legal_moves():
            wins = 0
            for _ in range(
                self.iterations
            ):
                state = initial_state.make_move(
                    move
                )
                result = self.simulate(
                    state
                )
                if result == 1:
                    wins += 1
            move_scores[move] = wins
        best_move = max(
            move_scores,
            key=move_scores.get
        )
        return best_move
    def simulate(self, state):
        current = state
        while not current.is_terminal():
            move = random.choice(
                current.legal_moves()
            )
            current = current.make_move(
                move
            )
        return current.utility()
        
  # ==========================================
# TEST CASES
# ==========================================

def run_test_case(
    name,
    board,
    player="X"
):
    print("\n")
    print("=" * 50)
    print(name)
    print("=" * 50)
    game = TicTacToe(
        board,
        player
    )
    game.display()
    print("=== Minimax ===")
    score, move = minimax(game)
    print(
        "Best Move:",
        move,
        "Score:",
        score
    )
    print("\n=== Alpha-Beta ===")
    score, move = alpha_beta_search(
        game
    )
    print(
        "Best Move:",
        move,
        "Score:",
        score
    )
    print(
        "\n=== Heuristic Alpha-Beta ==="
    )
    score, move = heuristic_alpha_beta(
        game,
        depth_limit=3
    )
    print(
        "Best Move:",
        move,
        "Score:",
        score
    )
    print(
        "\n=== Monte Carlo Tree Search ==="
    )
    mcts = MonteCarloTreeSearch(
        iterations=1000
    )
    move = mcts.search(game)
    print(
        "Best Move:",
        move
    )
if __name__ == "__main__":

    print("\n===================================")
    print("ADVERSARIAL SEARCH ALGORITHMS")
    print("===================================")

    print("\nChoose Board")
    print("1. Empty Board")
    print("2. Test Case 1")
    print("3. Test Case 2")
    print("4. Custom Board")
    choice = input("\nEnter Choice: ")

    if choice == "1":

        board = [
            " "," "," ",
            " "," "," ",
            " "," "," "
        ]

    elif choice == "2":

        board = [
            "O","O"," ",
            "X"," ","X",
            " ","X"," "
        ]

    elif choice == "3":

        board = [
            "X","X"," ",
            "O"," "," ",
            " "," "," "
        ]

    elif choice == "4":

        board = []

        print("\nEnter X, O or _")

        for i in range(9):

            value = input(
                f"Position {i}: "
            )
            if value == "_":
                value = " "

            board.append(value)
    else:

        board = [
            " "," "," ",
            " "," "," ",
            " "," "," "
        ]
    game = TicTacToe(board, "X")

    print("\nInitial Board")
    game.display()

    print("\n=== Minimax ===")
    score, move = minimax(game)
    print("Best Move:", move, "Score:", score)

    print("\n=== Alpha-Beta ===")
    score, move = alpha_beta_search(game)
    print("Best Move:", move, "Score:", score)

    print("\n=== Heuristic Alpha-Beta ===")
    score, move = heuristic_alpha_beta(
        game,
        depth_limit=3
    )
    print("Best Move:", move, "Score:", score)

    print("\n=== Monte Carlo Tree Search ===")
    mcts = MonteCarloTreeSearch(
        iterations=1000
    )

    move = mcts.search(game)

    print("Best Move:", move)
