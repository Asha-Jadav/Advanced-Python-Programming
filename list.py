import random
data=["geeta", "seeta", "ramayana", "rita", "priya", "ram", "shyam", "krishna", "janki", "radha"]
result=random.choice(data)
#print(result)
chance=1
print(data)
while(chance<=3):
    guess=input("Enter any Name from list : ")
    if(guess==result):
        print("Your choice is : ",guess)
        chance=chance+1
    elif(guess!=result):
        print("Wrong Choice")
        chance=chance+1

print("Name is : ", result)