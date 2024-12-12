import tkinter as tk
from tkinter import messagebox

class VotingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting System")

        self.candidates = ["BJP", "SP", "AAP"]
        self.votes = [0, 0, 0] 

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Select your candidate:")
        self.label.pack()

        self.var = tk.StringVar()

        for candidate in self.candidates:
            rb = tk.Radiobutton(self.master, text=candidate, variable=self.var, value=candidate)
            rb.pack()

        self.vote_button = tk.Button(self.master, text="Vote", command=self.vote)
        self.vote_button.pack()

        self.result_button = tk.Button(self.master, text="Show Results", command=self.show_results)
        self.result_button.pack()

    def vote(self):
        selected_candidate = self.var.get()

        if selected_candidate:
            index = self.candidates.index(selected_candidate)
            self.votes[index] += 1
            messagebox.showinfo("Success", f"You have voted for {selected_candidate}")
        else:
            messagebox.showwarning("Warning", "Please select a candidate to vote for.")

    def show_results(self):
        result_str = "Voting Results:\n"
        for i, candidate in enumerate(self.candidates):
            result_str += f"{candidate}: {self.votes[i]} votes\n"

        messagebox.showinfo("Results", result_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSystem(root)
    root.mainloop() 