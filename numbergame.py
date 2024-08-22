import random
chance=1
random_number=random.randint(1,50)
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

print("Number is : ", random_number)