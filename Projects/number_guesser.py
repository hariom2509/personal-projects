import random

# r = random.randrange(-5,11)
# print (r)
# r1 = random.randint(-5,11) #includes -5 and 11
# print (r1)

top_of_range = input ("Type a number: ")
if top_of_range.isdigit(): #isdigit() make sures the input is a digit or int
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a no. larger than 0")
        quit()
else:    
    print ("Please type a number")
    quit()
random_number = random.randint(0, top_of_range)
guesses = 0
# print (random_number)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:    
        print ("Please type a number")
        continue
    if user_guess == random_number:
        print("you got it right")
        break
    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("you were below the number")
        #print("you got it wrong")

print (f"you got it in {guesses} guesses")