# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name for each row 
        candidate_name=row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
# 3. Print the total votes.
print(total_votes)
# Print the candidate list
print(candidate_options)

    # Write some data to the file.
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("-------------------------\n")
    #txt_file.write("Arapahoe\n")
    #txt_file.write("Denver\n")
    #txt_file.write("Jefferson\n")