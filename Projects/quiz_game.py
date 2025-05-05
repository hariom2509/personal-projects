print("Welcome to the Game")

playing = input("Do you want to playy? ")
if playing.lower() != "yes":
    quit()

print("Okay! Lest play :) ")
score = 0

answer = input("What does cpu stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does gpu stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3)*100) + "%")
print(f"You got {score} questions correct.")
