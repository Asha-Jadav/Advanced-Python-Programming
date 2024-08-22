gender=input("Enter Your Gender : ")
gender=gender.lower()
if(gender=="male"):
    print("You are Male")
    age=int(Input("Enter your age : "))
    if(age>26):
        print("Your age is above 26")
        percentage = 25
    elif(age<26):
        print("Your are below 26")
        percentage = 10
    else:
        print("You are 26 years of age")
elif(gender=="female"):
    print("You are Female")
    choice=input("Enter your Choice")
    if(choice=="hollywood"):
        print("You like Hollywood Movies")
    elif(choice=="bollywood")
        print("You like Bollywood Movies")
    else
        print("Invalid Input")
else:
    print("Invalid Input")
    Market_price=int(input("Enter the Price of car : "))
    discount=(Market_price*percentage)*0.01
    actual_price=Market_price-discount
    print(f'Actual price you have to pay is : {actual_price}')
