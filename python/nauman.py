# # mini project nauman ke liye
# import tkinter as tk

# class VotingSystem:
#     def _init_(self, candidates):
#         self.candidates = candidates
#         self.votes = {candidate: 0 for candidate in candidates}

#     def vote(self, candidate):
#         if candidate in self.candidates:
#             self.votes[candidate] += 1
#             print(f"Voted for {candidate}")
#         else:
#             print("Invalid candidate")

#     def get_results(self):
#         return self.votes

# class VotingApp:
#     def _init_(self, master, voting_system):
#         self.master = master
#         self.master.title("Voting System")
#         self.voting_system = voting_system
#         self.label = tk.Label(master, text="Select a candidate:")
#         self.label.pack()
#         self.candidate_var = tk.StringVar()
#         self.candidate_var.set(voting_system.candidates[0])
#         self.candidate_menu = tk.OptionMenu(master, self.candidate_var, *voting_system.candidates)
#         self.candidate_menu.pack()
#         self.vote_button = tk.Button(master, text="Vote", command=self.vote)
#         self.vote_button.pack()
#         self.results_button = tk.Button(master, text="Show Results", command=self.show_results)
#         self.results_button.pack()
#     def vote(self):
#         selected_candidate = self.candidate_var.get()
#         self.voting_system.vote(selected_candidate)
#     def show_results(self):
#         results = self.voting_system.get_results()
#         for candidate, votes in results.items():
#             print(f"{candidate}: {votes} votes")

# if __name__ == "_main_":
#     candidates_list = ["Candidate A", "Candidate B", "Candidate C"]
#     voting_system = VotingSystem(candidates_list)
#     root = tk.Tk()
#     app = VotingApp(root, voting_system)
#     root.mainloop()