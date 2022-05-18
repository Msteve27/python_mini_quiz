print("Welcome to my computer quiz! Built with python.")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("OK, let's play! :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect")

answer = input("What does GCP stand for? ")
if answer.lower() == "google cloud platform":
    print("Correct!")
    score += 1
else: 
    print("Incorrect")
    
print("You got " + str(score) + " question(s) correct!")
print("You received a grade of " + str((score / 4) * 100) + "%" + " for this quiz!")
   