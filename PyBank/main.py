import csv
import os

#path to access file
budget_csv = os.path.join("..","PyBank","budget_data.csv")

#lists to store data
months = []
amount = []
monthly_change = []

#read in csv file

with open(budget_csv, 'r') as csvfile:
    #initialize csv and split on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skip header
    header = next(csvreader)

    # to get total months and amount of profit/loss, go  through all rows
    for row in csvreader:
        #append the date column to empty month list
        months.append(row[0])

        #append total of profit/loss column, type cast to ensure integer
        amount.append(int(row[1]))
        #print(months)
        #print(amount) 
    
    #to get change in monthly profit/loss, start new for loop
    for i in range(len(amount)-1):
        monthly_change.append((amount[i+1])-(amount[i]))
    
    #average changes
    monthy_average = round(sum(monthly_change)/ len(monthly_change),2)

    total_months = len(months)

    
    #max min values
    maxIncrease = max(monthly_change)
    maxDecrease = min(monthly_change)
    
    #print results to terminal
    print("Financial Analysis")
    print("--------------------------------------------")
    print("Total Months: " + str(total_months))
    print(f"Total: ${sum(amount)}")
    print(f"Average Change: ${monthy_average}")
    print(f"Greatest Increase in Profits : {str(months[monthly_change.index(maxIncrease)+1])} (${(str(maxIncrease))})")
    print(f"Greatest Decrease in Profits : {str(months[monthly_change.index(maxDecrease)+1])} (${(str(maxDecrease))})")
    
    #generate output text file
    output_file = os.path.join("..","PyBank","Summary.txt")

    with open(output_file, "w") as file:
        file.write("Financial Analysis" + "\n") #need end of line character
        file.write("--------------------------------------------" + "\n")
        file.write("Total Months" + str(total_months) + "\n")
        file.write(f"Total: ${sum(amount)}")
        file.write("\n")
        file.write(f"Average Change: ${monthy_average}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits : {str(months[monthly_change.index(maxIncrease)+1])} (${(str(maxIncrease))})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits : {str(months[monthly_change.index(maxDecrease)+1])} (${(str(maxDecrease))})")
        file.write("\n")











