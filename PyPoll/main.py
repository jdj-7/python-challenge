import csv
import os

# Create a path to the file
election_data_csv = os.path.join("c://Users/Owner/python_challenge/python-challenge/PyPoll/Resources/election_data.csv")

# Lists and dictionaries to store data
candidate_votes = {}  
candidates = []  
count_per = []  

# Variables
net_votes = 0  

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  

    csv_header = next(csv_reader)  # Skip the header
    print(f"Header: {csv_header}")

    for row in csv_reader:
        candidate = row[2]
        net_votes += 1

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

# Calculate percentages and prepare results
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / net_votes) * 100
    count_per.append(percentage)

# Print results
print(f"Total Votes: {net_votes}")
for i, candidate in enumerate(candidates):
    print(f"{candidate}: {count_per[i]:.3f}% ({candidate_votes[candidate]})")

# Find the winner
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")








