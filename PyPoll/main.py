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

vote_zero = 0
vote_one = 0
vote_two = 0

for candidate_vote in candidate_votes:
    if candidate_vote == candidate_list[0]:
        vote_zero = vote_zero + 1
    elif candidate_vote == candidate_list[1]:
        vote_one = vote_one + 1
    elif candidate_vote == candidate_list[2]:
        vote_two = vote_two + 1

zero_pct = vote_zero / total_votes
one_pct = vote_one / total_votes
two_pct = vote_two / total_votes

# determine winner
if vote_zero > vote_one and vote_zero > vote_two:
    winner = candidate_list[0]
elif vote_one > vote_zero and vote_one > vote_two:
    winnner = candidate_list[1]
elif vote_two > vote_zero and vote_two > vote_one:
    winner = candidate_list[2]

# print to terminal
print("Election Results")
print("---------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------------------------")
print(f"{candidate_list[0]}: {zero_pct: .3%} ({vote_zero})")
print(f"{candidate_list[2]}: {two_pct: .3%} ({vote_two})")
print(f"{candidate_list[1]}: {one_pct: .3%} ({vote_one})")
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
    txtfile.write(f"{candidate_list[0]}: {zero_pct: .3%} ({vote_zero})" + "\n")
    txtfile.write(f"{candidate_list[2]}: {two_pct: .3%} ({vote_two})" + "\n")
    txtfile.write(f"{candidate_list[1]}: {one_pct: .3%} ({vote_one})" + "\n")
    txtfile.write("---------------------------------------------------------" + "\n")
    txtfile.write(f"Winner: {winner}" + "\n")
    txtfile.write("---------------------------------------------------------")
