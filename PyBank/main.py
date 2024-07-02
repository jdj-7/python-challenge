
###Import the file
import csv
import os



###Create a path to that file
file_path = "c://Users/Owner/python_challenge/python-challenge/PyBank/Resources/budget_data.csv"
print (os.getcwd())

###Store Data
total = []
changes = []
months = []

##Variables
month = 0 
net_total = 0
greatest_increase = 0
greatest_decrease = 0


##Use the CSV read funtion to analyze the csv data
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimeter=",")
##Read and skip
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
  
  
    for row in csv_reader:
        month += 1
        months.append(row[0])

        ### get a total
        total.append(int(row[1]))

        ## net total function
        net_total += int([row[1]])

        ###find changes
    for i in range(1, len(total)):
        period_change = total[i] - total[i-1]

        changes.append(period_change)

        ###add change
        changes.append(period_change)

    ##avg change
    average_change - round(sum(changes) / len(changes),2)







