candidates = ["Alice", "Bob", "Charlie"]
votes = [0] * len(candidates)

while True:
    print("Candidates:")
    for i, name in enumerate(candidates):
        print(f"{i+1}. {name}")
    choice = input("Enter candidate number (or 'q' to quit): ")
    if choice.lower() == 'q':
        break
    if choice.isdigit() and 1 <= int(choice) <= len(candidates):
        votes[int(choice)-1] += 1
    else:
        print("Invalid choice")

max_votes = max(votes)
winners = [candidates[i] for i, v in enumerate(votes) if v == max_votes]

print("Vote tally:", dict(zip(candidates, votes)))
print("Winner(s):", ", ".join(winners))
