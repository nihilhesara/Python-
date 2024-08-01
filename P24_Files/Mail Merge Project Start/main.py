#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

PLACEHOLDER = "[name]"

# Change working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()              # Names turn into a list using readlines

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()            # Remove /n in the code 
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)      # Replace the name in the letter to the list of names 

        # Write to a new file
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)