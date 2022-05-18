print("Welcome to my computer quiz! Built with python. Please use lower case letters only.")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
    
print("OK, let's play! :) ")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else: 
    print("Incorrect, please try agian ")
    