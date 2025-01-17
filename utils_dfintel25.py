'''  ITERATION 5
Module: Step 5 of P1: Create a New Python Module
Author: Derek Fintel
I have modified this sample module to include new parameters below. 
Each commit of GitLab has the discrete changes noted.
Process:
In this iteration, I enhance the byline to include key details about skills
and client satisfaction scores. This makes the byline more informative and professional, 
ready for use in future projects.
'''
#####################################
# Import Modules at the Top
#####################################
import statistics
#####################################
# Declare global variables
#####################################
has_international_clients: bool = True
like_pop_music: bool = True
years_in_operation: int = 10
number_of_bathrooms: int = 17
average_client_satisfaction: float = 4.7
user_GitHub: str = "https://github.com/dfintel25"
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
number_of_wifi_routers: float = [2.2, 1.2, 3.2]
#####################################
# Calculate Basic Statistics
#####################################
# Calculate basic statistics using built-in functions and the statistics module
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)
min_wifi_score: float = min(number_of_wifi_routers)
max_wifi_score: float = max(number_of_wifi_routers)
stdev_wifi_score: float = statistics.stdev(number_of_wifi_routers)
#####################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Likes Pop Music:            {like_pop_music}   
Years in Operation:         {years_in_operation}
Number of Bathrooms:        {number_of_bathrooms}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
User Github:                {user_GitHub}
Number of Wifi Routers:     {number_of_wifi_routers}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
Standard Deviation:         {stdev_score:.2f}
Minimum Wifi Routers:       {min_wifi_score}
Maximum Wifi Routers:       {max_wifi_score}
Standard Deviation Wifi:    {stdev_wifi_score: .2f}
"""
#####################################
# Define the get_byline() Function
#####################################
def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline
   
#####################################
# Define a main() function for this module.
#####################################
def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
#####################################
# Conditional Execution
#####################################
if __name__ == '__main__':
    main()
