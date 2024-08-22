male=["ram", "shyam", "raj", "riyansh", "akash"]
female=["rita", "radha", "sita", "riya", "siya"]
name=input("Enter Any name : ")
if name in male:
    print(f"{name} is Male")
elif name in female:
    print(f"{name} is Female")
else:
    print("Try Again")

