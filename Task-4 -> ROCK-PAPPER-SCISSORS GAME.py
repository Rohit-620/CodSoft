import tkinter as tk
from tkinter import ttk
import random

# ---------------------------- CONSTANTS ------------------------------ #
BG_COLOR = "#f8edeb"        
TITLE_COLOR = "#ff5d8f"      
ROCK_COLOR = "#f0a500"        
PAPER_COLOR = "#00b4d8"       
SCISSOR_COLOR = "#ffafcc"    
SCORE_BG = "#e0fbfc"          
FONT_LARGE = ("Helvetica", 24, "bold")
FONT_MED = ("Helvetica", 16, "bold")
FONT_SMALL = ("Helvetica", 14)
CHOICES = ["Rock", "Paper", "Scissors"]
IMG = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# ---------------------------- MAIN APP ------------------------------- #
class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock • Paper • Scissors")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.user_score = 0
        self.comp_score = 0
        self._create_widgets()

    # ------------------------ GUI LAYOUT --------------------------- #
    def _create_widgets(self):
        # Title
        title = tk.Label(self, text="Rock  •  Paper  •  Scissors", fg=TITLE_COLOR,
                         bg=BG_COLOR, font=("Helvetica", 30, "bold"))
        title.pack(pady=10)

        # Rule diagram
        diagram_text = "🪨 ➡️ ✂️    ✂️ ➡️ 📄    📄 ➡️ 🪨"
        diagram = tk.Label(self, text=diagram_text, bg=BG_COLOR, font=FONT_MED)
        diagram.pack(pady=5)

        # Button frame
        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=20)

        # Rock button
        rock_btn = tk.Button(btn_frame, text=f"{IMG['Rock']}\nRock", bg=ROCK_COLOR,
                             font=FONT_MED, width=8, height=3, relief=tk.FLAT,
                             command=lambda: self._play_round("Rock"))
        rock_btn.grid(row=0, column=0, padx=10)

        # Paper button
        paper_btn = tk.Button(btn_frame, text=f"{IMG['Paper']}\nPaper", bg=PAPER_COLOR,
                              font=FONT_MED, width=8, height=3, relief=tk.FLAT,
                              command=lambda: self._play_round("Paper"))
        paper_btn.grid(row=0, column=1, padx=10)

        # Scissors button
        scissor_btn = tk.Button(btn_frame, text=f"{IMG['Scissors']}\nScissors", bg=SCISSOR_COLOR,
                                font=FONT_MED, width=8, height=3, relief=tk.FLAT,
                                command=lambda: self._play_round("Scissors"))
        scissor_btn.grid(row=0, column=2, padx=10)

        # Scoreboard
        score_frame = tk.Frame(self, bg=SCORE_BG, bd=2, relief=tk.GROOVE)
        score_frame.pack(pady=15, ipadx=10, ipady=5)

        self.user_score_lbl = tk.Label(score_frame, text="You: 0", bg=SCORE_BG, font=FONT_MED)
        self.user_score_lbl.grid(row=0, column=0, padx=20)

        self.comp_score_lbl = tk.Label(score_frame, text="Computer: 0", bg=SCORE_BG, font=FONT_MED)
        self.comp_score_lbl.grid(row=0, column=1, padx=20)

        # Result display
        self.result_lbl = tk.Label(self, text="Make your move!", bg=BG_COLOR, font=FONT_LARGE)
        self.result_lbl.pack(pady=20)

        # Play again / reset button
        reset_btn = tk.Button(self, text="🔄 Reset Scores", command=self._reset_game, font=FONT_SMALL,
                              bg="#ffffff", relief=tk.RIDGE)
        reset_btn.pack(pady=10)

    # ------------------------ GAME LOGIC --------------------------- #
    def _play_round(self, user_choice: str):
        comp_choice = random.choice(CHOICES)
        outcome = self._determine_winner(user_choice, comp_choice)

        # Update scores
        if outcome == "win":
            self.user_score += 1
            result_text = "You Win! 🎉"
            color = "#38b000"  # green
        elif outcome == "lose":
            self.comp_score += 1
            result_text = "You Lose 😔"
            color = "#d00000"  # red
        else:
            result_text = "It's a Tie 🤝"
            color = "#ff8800"  # orange

        # Update labels
        self.user_score_lbl.config(text=f"You: {self.user_score}")
        self.comp_score_lbl.config(text=f"Computer: {self.comp_score}")
        self.result_lbl.config(text=f"{result_text}\nYou chose {IMG[user_choice]}  |  Computer chose {IMG[comp_choice]}",
                               fg=color)

    @staticmethod
    def _determine_winner(user: str, comp: str) -> str:
        if user == comp:
            return "tie"
        if (user == "Rock" and comp == "Scissors") or \
           (user == "Scissors" and comp == "Paper") or \
           (user == "Paper" and comp == "Rock"):
            return "win"
        return "lose"

    def _reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.user_score_lbl.config(text="You: 0")
        self.comp_score_lbl.config(text="Computer: 0")
        self.result_lbl.config(text="Make your move!", fg="black")

# ---------------------------- RUN APP ------------------------------ #
if __name__ == "__main__":
    app = RPSApp()
    app.mainloop()
