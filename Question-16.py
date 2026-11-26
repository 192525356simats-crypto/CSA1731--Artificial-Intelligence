import math

def alpha_beta(state, depth, alpha, beta, maximizing_player):
    """
    Minimax algorithm with Alpha-Beta Pruning.

    Args:
        state: Current game state/board.
        depth (int): Maximum depth to search in the game tree.
        alpha (float): Best score the maximizing player can guarantee so far.
        beta (float): Best score the minimizing player can guarantee so far.
        maximizing_player (bool): True for AI/Maximizer, False for Opponent/Minimizer.

    Returns:
        tuple: (best_score, best_move)
    """
    # Base case: reached search depth limit or game is over
    if depth == 0 or state.is_terminal():
        return state.evaluate(), None

    best_move = None

    if maximizing_player:
        max_eval = -math.inf
        for move in state.get_legal_moves():
            child_state = state.make_move(move)
            eval_score, _ = alpha_beta(child_state, depth - 1, alpha, beta, False)
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
                
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cut-off (prune remaining branches)
                
        return max_eval, best_move

    else:
        min_eval = math.inf
        for move in state.get_legal_moves():
            child_state = state.make_move(move)
            eval_score, _ = alpha_beta(child_state, depth - 1, alpha, beta, True)
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
                
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cut-off (prune remaining branches)
                
        return min_eval, best_move
