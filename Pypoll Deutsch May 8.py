#Pypoll Deutsch

#Define Variables
total_votes = 0
Candidates_votes = {}
list_of_candidates = []

winning_candidate = ""
winning_count = 0


"""
The total number of votes cast ()
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
"""

#Import and read election file

import csv
with open(r"C:\users\deuts\Phw\election_data.csv") as file:
    reader = csv.reader(file)
    header = next(reader) #read the header row
   
   
    for row in reader:
        
        #Calculate total votes
        total_votes += 1

        # Get Candidate name 
        candidate_name = row[2]
        
        if candidate_name not in list_of_candidates:
            list_of_candidates.append(candidate_name)
            
            # Initialize the candidates votes
            Candidates_votes[candidate_name] = 0
        
        # Increase the candidate vote by 1 
        Candidates_votes[candidate_name] =  Candidates_votes[candidate_name] + 1
        
print(Candidates_votes)

with open('output.txt', "w") as txt_file:
    
    election_results = (
        f"Total Votes: {total_votes} \n"
        
        )
    txt_file.write(election_results) 
    
    for candidates in Candidates_votes:
        votes = Candidates_votes.get(candidates)
        percentage_votes = votes/total_votes
        percentage_votes ="%{:,.2f}".format(percentage_votes)
        
        
        if votes > winning_count:
            winning_candidate = candidates
            winning_count = votes
        
        voting_results = (
                f" Candidate: {candidates} \n"
                f"Percentage votes: {percentage_votes} \n"
                f"Total Votes : {votes} \n"
                
            )
        
        txt_file.write(voting_results)
        
    winner = (
        f"The winner is: {winning_candidate} \n"
        )
    txt_file.write(winner)
#Loop through file and count votes by candidate: Correy, Khan, Li, O'Tooley




        
   