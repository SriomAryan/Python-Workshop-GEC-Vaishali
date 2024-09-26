import tkinter as tk
from tkinter import messagebox

class SimpleEVM:
    def _init_(self, root):
        self.root = root
        self.root.title("Simple EVM Voting System")
        
        # Variables to track the vote counts
        self.candidate1_votes = 0
        self.candidate2_votes = 0
        
        # Create and place buttons
        self.button_candidate1 = tk.Button(root, text="Vote for Candidate 1", command=self.vote_candidate1, width=25, height=3)
        self.button_candidate1.pack(pady=10)
        
        self.button_candidate2 = tk.Button(root, text="Vote for Candidate 2", command=self.vote_candidate2, width=25, height=3)
        self.button_candidate2.pack(pady=10)
        
        # Label to show the vote results
        self.result_label = tk.Label(root, text="Vote Results will appear here", font=("Arial", 14))
        self.result_label.pack(pady=20)
    
    # Method to handle vote for candidate 1
    def vote_candidate1(self):
        self.candidate1_votes += 1
        self.update_results()
    
    # Method to handle vote for candidate 2
    def vote_candidate2(self):
        self.candidate2_votes += 1
        self.update_results()
    
    # Method to update and display the vote results
    def update_results(self):
        results = f"Candidate 1: {self.candidate1_votes} votes\nCandidate 2: {self.candidate2_votes} votes"
        self.result_label.config(text=results)

# Main window setup
if _name_ == "_main_":
    root = tk.Tk()
    app = SimpleEVM(root)
    root.mainloop()
