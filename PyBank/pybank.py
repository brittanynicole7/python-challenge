#Import Dependencies
import os
import csv

# Store path to csv file and txt file
pybank_csv = os.path.join('Resources', 'budget_data.csv')
pybank_output = os.path.join('analysis', 'budget_analysis.txt')

# Open and read csv file
with open (pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    # Skip first row
    next(csv_reader)

#Set variables outside the loop
    first_row = next(csv_reader)
    number_of_months = 1
    net_total = int(first_row[1])
    last_pl = int(first_row[1])
    sum_change = []
    months = []
    greatest_increase = ["",0]
    greatest_decrease = ["", 99999999999999999999]
    
        

    #Start the loop
    for row in csv_reader: 
        #Calculation for total number of months
        number_of_months = number_of_months + 1 
        #Calculation for net total
        net_total += int(row[1])
        #Set p and l for index row 1. Calculation for change between current month profit and loss and last month profit and loss
        change = int(row[1]) - last_pl
        last_pl = int(row[1])
        # Calculation for total change
        sum_change += [change]
        # Set months to index row 0 and add months
        months += row[0]
        

        # Conditional to determine the greatest increase
        if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = row[0]

        # Conditional to determine the greatest decrease
        if change < greatest_decrease[1]:
            greatest_decrease[1] = change 
            greatest_decrease[0] = row[0]

    # Store average change as a variable 
    average_change = round((sum(sum_change)/len(sum_change)), 2)

    #Output to txt file
    with open (pybank_output, "w") as output_file:

        #Format txt file
        pybank_txt = (f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {number_of_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

        #Print Output
        print(pybank_txt)

        #Write the output to the txt file
        output_file.write(pybank_txt)




        




