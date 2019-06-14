import os
import csv

elections_file = os.join.path("..","PyPoll", "election_data.csv")

#variables to store data
total_votes = 0
candidates = []

with open(elections_file,newline="") as elections:
    electionreader = csv.reader(elections, delimiter = ",")
header = next(electionreader)

#to count total number of votes cast
for row in electionreader:
    total_votes +=1
    #append names to candidates
    candidates.append(row[2])
    
    

