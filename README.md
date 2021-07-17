# Election_Analysis - Module 3 Challenge
##  **Overview**
  This task had us take a good look into election data and to help a client in determining the winner of an election.  The coding language used for this task was python as per the clients instructions.  We also made use of the command prompt and git bash terminals to commit/push and pull files from the projects GitHub repository.  We utilized different data types in python, as well as pulling information from a CSV file.  The results were then printed into the terminal for immediate review as well as printing them to a text file that could be easily accessed by any and all needed parties.  This code could easily be modified to be more generalized for use in any election, not just this one in particular.
  
##  **Results**
https://github.com/wprich/Election_Analysis/blob/main/PyPoll_Challenge.py
https://github.com/wprich/Election_Analysis/blob/main/analysis/election_analysis.txt
```

Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
```
```
    # -*- coding: UTF-8 -*-
    # Add our dependencies.
import csv
import os

     # Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
     # Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Initialize a total vote counter.
total_votes = 0

    # Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

    # 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

    # Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

    # 2: Track the largest county and county voter turnout and county percentage.
largest_county = ""
largest_county_votes = 0

    # Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]
        
        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
 

    # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        c_votes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        county_results  = (
            f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (c_votes > largest_county_votes):
            largest_county_votes = c_votes
            largest_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
            county_vote_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(county_vote_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_vote_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
   
   ```
    
 - After looking over the CSV file and writing the pseudo code, it was determined by the client that some things were going to need to be gathered in order to call the project a success.  First being the total number of votes.  By declaring a variable called total_votes and setting it to zero before any loops, we could then count each vote to get the total. 
 ```
     # Initialize a total vote counter.
total_votes = 0

     # Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Read the header
    header = next(reader)
    
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        Total Votes: 369,711
  ```
  
- Then by using some simple expressions and variable declaration, we figured out the total percentage of votes for each county in relation to the total number of votes cast.  This made use of the dictionary and list data types as well as the append function.  This particular set of data had only three counties to pull from so all were accounted for in the results.

  ```
      # 1: Create a county list and county votes dictionary.
      county_list = []
      county_votes = {}
      
      # 4a: Write an if statement that checks that the
      # county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
            
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
                # 6b: Retrieve the county vote count.
        c_votes = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        county_results  = (
            f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
            
        County Votes:
        Jefferson: 10.5% (38,855)
        Denver: 82.8% (306,055)
        Arapahoe: 6.7% (24,801)
    ```
    
 -  The client was also interested in finding out which county had the most voters turn up on voting day and how much that counties votes were in relation to the total number of votes cast.  This was determined by referencing the number of county votes and comparing to a variable, largest_county_votes, set to 0 at the start of the code.  It was determined that Denver had the greatest voter turnout at the end of the analysis.

    ```
        # 2: Track the largest county and county voter turnout and county percentage.
        largest_county = ""
        largest_county_votes = 0
        
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (c_votes > largest_county_votes):
            largest_county_votes = c_votes
            largest_county = county_name
            
        # 7: Print the county with the largest turnout to the terminal.
            county_vote_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(county_vote_summary)
    
    Largest County Turnout: Denver
    ```
    
 -  As with any election, there has to be a winner.  This particular election was decided by popular vote therefore there was not an electoral college or electors in this process.  Upon getting the total number of votes and determining the candidate with the most amount, we could determine a winner and submit the findings to the board of elections.  The total number of votes in this election was 369,711.

    ```
        # Get the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
        
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        Charles Casper Stockham: 23.0% (85,213)
        Diana DeGette: 73.8% (272,892)
        Raymon Anthony Doane: 3.1% (11,606)

    ```

 -  This election data and code shows us that the winner with the most votes was Diana DeGette, with 73.8% of the vote, or 272,892 votes.

    ```
     # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    ```
    
##  **Summary**

  This code was a good deep dive into the python programming language and showed its versatility as well as its usefulness in looking over the biggest data set that we've seen to date, nearly 370,000 rows.  This code could even be improved upon to make it more generalized and possibly used for other elections.  We would have to specify the election would have to be a popular vote one and not an election that utilises the electoral college.  One way the script could change is the total votes variable could be calculated differently if each counties total votes were added together to get the total votes cast, thereby not needing to declare it at the start.  This would eliminate the count having to be tallied in the main for loop at all.
  ```
  
    values = county_votes.values()
    total_votes = sum(values)
    print(total_votes)
    
    369711
    
  ```
  This code gets us to the same result of 369,711 votes cast in the election.  This could be further generalized to breakdown the election by district if going to a state election.  Each districts total vote count could be achieved by adding the distrcits individual county votes together.  The only thing that would need to be known beforehand would be each districts breakdown and which counties fell into which district. This could then be displayed in the code using a combination of lists and dictionaries.  These district votes could then be added up to get the total votes cast in the state.  You could then analyze which district makes up the greatest voter count to the total as well as the individual county with the most votes cast as well.  
  
  Something else you could use to try and make this code a little better is telling anyone who were to look at the data how many counties and how many candidates there were in the election results.  Since some states and/or districts have a plethora of counties, depending on geography.  This could be beneficial to counting each county from the results page.  Also, there is no telling how many candidates can appear for one or more offices during an election.  So having a total amount show up in the results instead of manually counting can save time and make the presentation look more clean.
  
  ```
  
  print("There were a total of " + str(len(county_list)) + " counties.")
  print("There were a total of " + str(len(candidate_options)) + " candidates.")
  
  There were a total of 3 counties.
  There were a total of 3 candidates.
  
  ```
  
  Another way this code could be improved to help voter demographics is stating which political party each candidate is for, either republican, democrat, or independent, etc.  This could help further increase accuracy in audits of the results as well as help in creating statistical models for future politicians and/or companies to get voting demographics and plan out campaign strategies. All of these improvements would depend on the man power needed to make the changes and also the time in between elections to determine if any need for the code exists at all.   
