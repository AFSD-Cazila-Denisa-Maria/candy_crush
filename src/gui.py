import tkinter as tk
import time

COLORS = {
    0: "#ffffff",
    1: "#ff4d4d",
    2: "#ffd11a",
    3: "#4dff4d",
    4: "#4da6ff"
}

class GameGUI:
    def __init__(self, engine):
        self.engine = engine
        self.selected = None
        self.auto = False
        self.paused = False

        self.root = tk.Tk()
        self.root.title("CandyCrush Automator - Tk")
        self.root.resizable(False, False)

        # ===== TOP BAR =====
        top = tk.Frame(self.root, pady=6)
        top.pack()

        self.score_lbl = tk.Label(top, text="Score: 0", font=("Arial", 11, "bold"))
        self.score_lbl.pack(side="left", padx=8)

        self.level_lbl = tk.Label(top, text="Level: 1", font=("Arial", 11, "bold"))
        self.level_lbl.pack(side="left", padx=8)

        tk.Button(top, text="Pause", width=7, command=self.toggle_pause).pack(side="left", padx=4)
        tk.Button(top, text="Step", width=7, command=self.step).pack(side="left", padx=4)
        tk.Button(top, text="Reset", width=7, command=self.reset).pack(side="left", padx=4)
        tk.Button(top, text="Auto", width=7, command=self.toggle_auto).pack(side="left", padx=4)

        # ===== GRID =====
        grid = tk.Frame(self.root, padx=6, pady=6)
        grid.pack()

        self.cells = []
        for r in range(11):
            row = []
            for c in range(11):
                lbl = tk.Label(
                    grid,
                    width=4,
                    height=2,
                    bg="white",
                    relief="solid",
                    borderwidth=1
                )
                lbl.grid(row=r, column=c, padx=1, pady=1)
                lbl.bind("<Button-1>", lambda e, x=r, y=c: self.click(x, y))
                row.append(lbl)
            self.cells.append(row)

        self.update()

    # CLICK HANDLING
    def click(self, r, c):
        if self.paused:
            return

        if self.selected is None:
            self.selected = (r, c)
            self.cells[r][c].config(relief="sunken")
            return

        r1, c1 = self.selected
        self.cells[r1][c1].config(relief="solid")

        if self.engine.try_swap((r1, c1), (r, c)):
            self.animate_cascade()

        self.selected = None
        self.update()

    #  ANIMATION
    def animate_cascade(self):
        while self.engine.cascade_step():
            self.update()
            self.root.update()
            time.sleep(0.12)

    #  BUTTON ACTIONS
    def toggle_pause(self):
        self.paused = not self.paused

    def step(self):
        if not self.paused:
            self.animate_cascade()

    def reset(self):
        self.engine.board.__init__()
        self.engine.score = 0
        self.engine.level = 1
        self.update()

    def toggle_auto(self):
        self.auto = not self.auto
        if self.auto:
            self.auto_play()

    def auto_play(self):
        if not self.auto or self.paused:
            return

        moved = False
        for r in range(11):
            for c in range(11):
                if c + 1 < 11 and self.engine.try_swap((r, c), (r, c + 1)):
                    self.animate_cascade()
                    moved = True
                    break
            if moved:
                break

        self.root.after(400, self.auto_play)

    #UPDATE UI
    def update(self):
        for r in range(11):
            for c in range(11):
                val = self.engine.board.grid[r][c]
                self.cells[r][c].config(bg=COLORS[val])

        self.score_lbl.config(text=f"Score: {self.engine.score}")
        self.level_lbl.config(text=f"Level: {self.engine.level}")

    def run(self):
        self.root.mainloop()
