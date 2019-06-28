import os
import csv

elections_file = os.path.join("..","PyPoll", "election_data.csv")

#variables to store data
total_votes = 0
cand_dict = {} 


with open(elections_file, 'r') as elections:
    electionreader = csv.reader(elections)
    next(electionreader, None)

#to count total number of votes cast
    for row in electionreader:
        total_votes +=1
    #append names from col 3 to dict, keep track if voted for by adding to counter
        if row[2] in cand_dict.keys():
            cand_dict[row[2]] = cand_dict[row[2]] + 1
        else:
            cand_dict[row[2]] = 1

#empty lists
candidates = []
vote_count = []

#iterate over dict, append dict vals and keys to respective lists
for key,value in cand_dict.items():
    candidates.append(key)
    vote_count.append(value)

#new list for percent
percent = []
for count in vote_count:
    percent.append(round(count/total_votes*100,1))
#zip all into tuples
data = list(zip(candidates, vote_count, percent))   

win =[]
for name in data:
    if max(vote_count) == name[1]:
        win.append(name[0])
winner = win[0]

if len(win) >1 :
    for champ in range(1,len(Win)):
        winner = winner + ", " + win[champ]

#print
output_file = os.path.join("..","PyPoll", "Summary.txt")
with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())