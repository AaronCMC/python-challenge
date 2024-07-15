# import os module to create file paths across operating systems
import os

# import module for reading csv files
import csv

# set path
csvpath = os.path.join('Resources', 'election_data.csv')

# read csv
votes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)


    for vote in csvreader:
        votes.append(vote)

# determine total vote count
total_votes = len(votes)

# determine candidates and polling (total amount & percentage by candidate)
candidate_votes = []

for vote in votes:
    candidate_votes.append(vote[2])

candidate_list = list(set(candidate_votes))

vote_Charles = 0
vote_Raymon = 0
vote_Diana = 0

for candidate_vote in candidate_votes:
    if candidate_vote == "Charles Casper Stockham":
        vote_Charles = vote_Charles + 1
    elif candidate_vote == "Raymon Anthony Doane":
        vote_Raymon = vote_Raymon + 1
    elif candidate_vote == "Diana DeGette":
        vote_Diana = vote_Diana + 1

Charles_pct = vote_Charles / total_votes
Raymon_pct = vote_Raymon / total_votes
Diana_pct = vote_Diana / total_votes

# determine winner
if vote_Charles > vote_Raymon and vote_Charles > vote_Diana:
    winner = "Charles Casper Stockham"
elif vote_Raymon > vote_Charles and vote_Raymon > vote_Diana:
    winnner = "Raymon Anthony Doane"
elif vote_Diana > vote_Charles and vote_Diana > vote_Raymon:
    winner = "Diana DeGette"

# print to terminal
print("Election Results")
print("---------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------------------------")
print(f"Charles Casper Stockham: {Charles_pct: .3%} ({vote_Charles})")
print(f"Diana DeGette: {Diana_pct: .3%} ({vote_Diana})")
print(f"Raymon Anthony Doane: {Raymon_pct: .3%} ({vote_Raymon})")
print("---------------------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------------------")

# write .txt file
txt_path = os.path.join('analysis', 'PyPoll_results.txt')

with open(txt_path, 'w') as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("---------------------------------------------------------" + "\n")
    txtfile.write(f"Total Votes: {total_votes}" + "\n")
    txtfile.write("---------------------------------------------------------" + "\n")
    txtfile.write(f"Charles Casper Stockham: {Charles_pct: .3%} ({vote_Charles})" + "\n")
    txtfile.write(f"Diana DeGette: {Diana_pct: .3%} ({vote_Diana})" + "\n")
    txtfile.write(f"Raymon Anthony Doane: {Raymon_pct: .3%} ({vote_Raymon})" + "\n")
    txtfile.write("---------------------------------------------------------" + "\n")
    txtfile.write(f"Winner: {winner}" + "\n")
    txtfile.write("---------------------------------------------------------")
