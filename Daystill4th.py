##MICHAEL_BENNETT
##SDEV300_7380
##Professor_Zachery_Fair
##Week2_assignment2_How_Many_Days_From_Today__Until_July4,2025?
##3/28/2023


import datetime


# Ask the user if they're looking forward to the fireworks
response = input("Are you looking forward to the fireworks on the Fourth of July? (yes/no) ")

# Get the current date and time
now = datetime.datetime.now()

# Get the date of the next Fourth of July
fourth_of_july = datetime.datetime(2025, 7, 4)

# Calculate the difference between the current date and the Fourth of July
difference = fourth_of_july - now

# Display the results
if response == "yes":
    print("Great! You have {} days to look forward to the fireworks on July 4,2025.".format(difference.days))
else:
    print("No worries, you still have {} days to change your mind.".format(difference.days))