import csv
import os
from board import Board
from engine import Engine

TARGET = 10000
MAX_SWAPS = 300

def has_valid_move(engine):
    b = engine.board
    for r in range(b.rows):
        for c in range(b.cols):
            if c + 1 < b.cols and engine.try_swap((r,c),(r,c+1)):
                return True
            if r + 1 < b.rows and engine.try_swap((r,c),(r+1,c)):
                return True
    return False

def run_games(games=100, out="results/summary.csv"):
    os.makedirs("results", exist_ok=True)

    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "game_id","points","swaps",
            "total_cascades","reached_target",
            "stopping_reason","moves_to_10000"
        ])

        for gid in range(games):
            board = Board()
            engine = Engine(board)

            cascades = 0
            swaps = 0
            moves_to_10000 = ""
            reached = False

            while engine.cascade_step():
                cascades += 1

            while swaps < MAX_SWAPS:
                if engine.score >= TARGET:
                    reached = True
                    moves_to_10000 = swaps
                    break

                if not has_valid_move(engine):
                    break

                swaps += 1
                while engine.cascade_step():
                    cascades += 1

            reason = "REACHED_TARGET" if reached else "NO_MOVES"

            w.writerow([
                gid, engine.score, swaps,
                cascades, reached, reason, moves_to_10000
            ])
