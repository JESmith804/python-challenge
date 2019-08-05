import os
import csv

# Path to collect data from the Resources folder
csvpath =  os.path.join ('..', 'PyBank', 'budget_data.csv')

# Create data lists
months = []
net_total = []
avg_changes = []

# set initial variable values
inc = 0
dec = 0
i = 0
j = 0

# opens input file, removes header row and loops through the remaining rows
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # add month to list 'months'
        months.append(row[0])
        # add Profit/Loss to list 'profLoss'
        net_total.append(int(row[1]))
# The net total amount of "Profit/Losses" over the entire period
profit_loss = sum(net_total)

# creating a list of all changes and calculating the average
while i < (len(net_total)-1):
    currChg = net_total[i+1] - net_total[i]
    avg_changes.append(currChg)
    i = i + 1
avgChg = (sum(avg_changes))/(len(avg_changes))
avgChg = round(avgChg, 2)


# finds the greatest profit and loss and captures the index for the month it occurred
while j < (len(avg_changes)):
    if avg_changes[j] > inc:
        inc = avg_changes[j]
        incMon = j + 1
    if avg_changes[j] < dec:
        dec = avg_changes[j] 
        decMon = j + 1
    j = j + 1

# print output in terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(f"{profit_loss:,d}"))
print("Average Change: $" + str(avgChg))
print("Greatest Increase in Profits: " + str(months[incMon]) + " ($" + str((f"{inc:,d}")) + ")")
print("Greatest Decrease in Profits: " + str(months[decMon]) + " ($" + str((f"{dec:,d}")) + ")")


# create output text file and write output into the file
output_file = os.path.join("output.txt")
writer = open(output_file, 'w+')    
writer.write("Financial Analysis\n")
writer.write("----------------------------\n")
writer.write("Total Months: " + str(len(months)) + "\n")
writer.write("Total: $" + str(f"{profit_loss:,d}") + "\n")
writer.write("Average Change: $" + str(avgChg) + "\n")
writer.write("Greatest Increase in Profits: " + str(months[incMon]) + " ($" + str((f"{inc:,d}")) + ")\n") 
writer.write("Greatest Decrease in Profits: " + str(months[decMon]) + " ($" + str((f"{dec:,d}")) + ")\n")