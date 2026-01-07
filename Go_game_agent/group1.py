from game.go import Board
from typing import List, Optional
import math
class MinimaxAgent:
    """
    Minimax-based agent with alpha-beta pruning
    for a Go-like board game.
    """
    def __init__(self, color: int, max_depth: int = 3):
        self.color = color
        self.max_depth = max_depth
        self.nodes_evaluated = 0

    def evaluate(self, board: Board) -> int:
        """
        Basic board evaluation function.
        """
        if board.winner == self.color:
            return 1
        elif board.winner is not None:
            return -1
        return 0

    def minimax(
        self,
        board: Board,
        depth: int,
        alpha: float,
        beta: float,
        maximizing: bool
    ) -> int:
        """
        Minimax algorithm with alpha-beta pruning.
        """
        self.nodes_evaluated += 1

        if board.winner is not None or depth >= self.max_depth:
            return self.evaluate(board)

        actions = board.get_legal_actions()
        if not actions:
            return 0

        if maximizing:
            value = -math.inf
            for action in actions:
                new_board = board.copy()
                new_board.put_stone(action)
                value = max(
                    value,
                    self.minimax(new_board, depth + 1, alpha, beta, False)
                )
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = math.inf
            for action in actions:
                new_board = board.copy()
                new_board.put_stone(action)
                value = min(
                    value,
                    self.minimax(new_board, depth + 1, alpha, beta, True)
                )
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def choose_best_action(
        self,
        board: Board,
        actions: List
    ) -> Optional:
        """
        Selects the best action using minimax search.
        """
        best_score = -math.inf
        best_action = None

        for action in actions:
            new_board = board.copy()
            new_board.put_stone(action)
            score = self.minimax(
                new_board,
                depth=1,
                alpha=-math.inf,
                beta=math.inf,
                maximizing=False
            )
            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    def get_action(self, board: Board):
        """
        Public method used by the game engine.
        """
        self.nodes_evaluated = 0
        actions = board.get_legal_actions()

        if not actions:
            return None

        action = self.choose_best_action(board, actions)

        print(f"Nodes evaluated: {self.nodes_evaluated}")
        return action
