#Import Dependencies
import os
import csv

# Store path to csv file and txt file
pypoll_csv = os.path.join('Resources', 'election_data.csv')
pypoll_output = os.path.join('analysis', 'election_analysis.txt')

# Create empty candidate dictionary and list for later to store information about individual candidates
cand_dict = {}
cand_list = []

# Open and read csv file
with open (pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    # Skip first row
    next(csv_reader)

# Set variables outside the loop 
    first_row = next(csv_reader)
    number_of_votes = 1

 # Start the loop
    for row in csv_reader: 
        # Calculation for total number of votes
        number_of_votes = number_of_votes + 1 
        # Store value for candidate name
        name = row[2]

        # Conditional for adding candidate name, switching to next candidate, and adding number of votes per candidate
        if name not in cand_list:
          cand_list.append(name)
          cand_dict [name] = 0 
        cand_dict [name] += 1   

    # Store value for percentage of votes and total number of votes per candidate
    result = {key: round((value / number_of_votes) * 100,3) for key, value in cand_dict.items()}

    # Store value for candidate with the highest number of votes
    max_value = max(cand_dict, key=cand_dict.get)
    
# Output to txt file
with open (pypoll_output,"w") as output_file:

    # Print first part with number of votes. Write to txt file.
    pypoll_output_1 =(f"Election Results\n" 
    f"----------------------------\n"
    f"Total Votes: {number_of_votes}\n"
    f"----------------------------\n")
    print (pypoll_output_1)
    output_file.write(pypoll_output_1)

    # Print and format second part with candidate names, total votes, and percentages. Write to txt file.
    for k,v in cand_dict.items():
      pypoll_output_2 = (f"{k}: {result[k]}% ({v})\n")
      print(pypoll_output_2)
      output_file.write(pypoll_output_2)

    # Print third part with Winner name and votes. Write to txt file. 
    pypoll_output_3 = (f"-------------------------\n"
    f"Winner: {max_value}\n"
    f"-------------------------")
    print (pypoll_output_3)
    output_file.write(pypoll_output_3)

