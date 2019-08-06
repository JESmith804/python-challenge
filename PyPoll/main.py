import os
import csv

# input file path
csvpath =  os.path.join ('..', 'PyPoll', 'election_data.csv')

# Lists to store data
voterIDs = []
candidates = []
voteCounts = []

# set initial values
i = 0
j = 0
k = 0
win = 0

# opens input file, removes header row and loops through the remaining rows
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # add each vorer ID to list 'voterIDs'; it's length is the total number of votes
        voterIDs.append(row[0])
        # add the candidate for each vote to a list
        candidates.append(row[2])

# remove duplicates from candidate list
candidates = list( dict.fromkeys(candidates))

#loops through candidates list 
while i < (len(candidates)):
    # opens input file, removes header row and loops through the remaining rows
    with open(csvpath, newline= "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        voteCnt = 0
        for row in csvreader:
            # counts the number of votes for each candidate
            if candidates[i] == row[2]:
                voteCnt = voteCnt + 1
    # adds vote count for each cadidate to list            
    voteCounts.append(voteCnt)
    i = i + 1


# print output in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(f"{(len(voterIDs)):,d}"))
print("-------------------------")
# loops and prints results for each canditates and stores the index of the highest vote count
while j < (len(candidates)):
    if voteCounts[j] > win:
        win = voteCounts[j]
        winCand = j
    pct = ((voteCounts[j])/(sum(voteCounts)))*100
    pct = round(pct, 2)
    print(candidates[j] + ": " + str(pct) + "%  (" + str(f"{(voteCounts[j]):,d}") + ")")
    j = j + 1
print("-------------------------")
# uses the index of the highest vote count to return the name of the winning candidate
print("Winner:  " + candidates[winCand])
print("-------------------------")


# create output text file and write output into the file
output_file = os.path.join("output.txt")
writer = open(output_file, 'w+') 
writer.write("Election Results\n")
writer.write("-------------------------\n")
writer.write("Total Votes: " + str(f"{(len(voterIDs)):,d}") + "\n")
writer.write("-------------------------\n")
while k < (len(candidates)):
    pct = ((voteCounts[k])/(sum(voteCounts)))*100
    pct = round(pct, 2)
    writer.write(candidates[k] + ": " + str(pct) + "%  (" + str(f"{(voteCounts[k]):,d}") + ")\n")
    k = k + 1
writer.write("-------------------------\n")
writer.write("Winner:  " + candidates[winCand] + "\n")
writer.write("-------------------------\n")