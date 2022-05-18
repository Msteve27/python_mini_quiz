print("Welcome to my computer quiz! Built with python.")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("OK, let's play! :) ")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else: 
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
else: 
    print("Incorrect")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
else: 
    print("Incorrect")

answer = input("What does GCP stand for? ")
if answer.lower() == "google cloud platform":
    print("Correct!")
else: 
    print("Incorrect")
   