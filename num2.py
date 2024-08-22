import random
chance=1

l=int(input("Enter the lower limit : "))
u=int(input("Enter the upper limit : "))
random_number=random.randint(l,u)
while(chance<=3):
    guess=int(input("Guess the Number : "))
    if(guess==random_number):
        print("You won the game!")
    elif(guess<random_number):
        print("You have entered lower value")
        chance=chance+1
    elif(guess>random_number):
        print("You have entered higher value")
        chance=chance+1