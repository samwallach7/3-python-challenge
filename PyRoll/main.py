import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

ballot_id = []
county = []
candidate = []
candidate_CCS = "Charles Casper Stockham"
votes_CCS = 0
candidate_DD = "Diana DeGette"
votes_DD = 0
candidate_RAD = "Raymon Anthony Doane"
votes_RAD = 0

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_headers = next(csvreader)
    print(f'"CSV HEADER: {csv_headers}')
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        if row[2] == candidate_CCS:
            votes_CCS += 1
        elif row[2] == candidate_DD:
            votes_DD += 1
        elif row[2] == candidate_RAD:
            votes_RAD += 1


total_votes = len(ballot_id)
per_total_votes_CCS = round((votes_CCS / total_votes) * 100, 3)
per_total_votes_DD = round((votes_DD / total_votes) * 100, 3)
per_total_votes_RAD = round((votes_RAD / total_votes) * 100, 3)


if votes_CCS > votes_DD and votes_CCS > votes_RAD:
    election_winner = candidate_CCS
elif votes_DD > votes_CCS and votes_DD > votes_RAD:
    election_winner = candidate_DD
elif votes_RAD > votes_CCS and votes_RAD > votes_DD:
    election_winner = candidate_RAD


# Final output -----------------------------------
print(f'Election Results')
print(f'-----------------------------------')
print(f'Total Votes: {total_votes}')
print(f'-----------------------------------')
print(f'{candidate_CCS}: {per_total_votes_CCS}% ({votes_CCS})')
print(f'{candidate_DD}: {per_total_votes_DD}% ({votes_DD})')
print(f'{candidate_RAD}: {per_total_votes_RAD}% ({votes_RAD})')
print(f'-----------------------------------')
print(f'Winner: {election_winner}')
print(f'-----------------------------------')

lines = ["Election Results", 
         "---------------------------------", 
         (f'Total Votes: {total_votes}'),
         "---------------------------------", 
         (f'{candidate_CCS}: {per_total_votes_CCS}% ({votes_CCS})'), 
         (f'{candidate_DD}: {per_total_votes_DD}% ({votes_DD})'), 
         (f'{candidate_RAD}: {per_total_votes_RAD}% ({votes_RAD})'),
         "---------------------------------",
         (f'Winner: {election_winner}'),
         "---------------------------------"]
output_file = os.path.join('analysis', "election_results.txt")
with open(output_file, "w") as f:
    for line in lines:
        f.write(line)
        f.write('\n')