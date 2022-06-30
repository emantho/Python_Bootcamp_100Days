#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#%% Opening the letter template absolute path
with open(r"/home/eder/projects/Python_Bootcamp_100Days/Day-24/Input/Letters/starting_letter.txt", mode="r") as letter:
    content = letter.read()
    print(content)

#%% Opening the letter template relative path
with open(r"Input/Letters/starting_letter.txt", mode="r") as letter:
    content = letter.read()
    print(content)
# %% Opening names relative path
with open(r"Input/Names/invited_names.txt", mode="r") as letter:
    content = letter.read()
    print(content)
# %%
letter = open(r"Input/Letters/starting_letter.txt", mode="r")
content = letter.readlines()
print(content)
# %%
