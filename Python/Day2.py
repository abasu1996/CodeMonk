height = int(input("Write Down your Height in CM "))
weight = int(input("Write Down your Weight in Kg"))

BMI = weight / (height * height)

if BMI < 18.5:
    print("You are under weight")
elif BMI <22 and BMI > 22.5:
    print("You are good to go")
    
year = int(input("Please enter the year..."))



if (year%4) == 0:
    if (year%100) == 0:
        if (year%400) ==0:
            print("LY")
        else:
            print("Not a LY")   
    else:
        print("It is a LY")        
else:
    print("Not a LY")


##Succession of IF Statement

print("Welcome to Pizza Shop..!!")

size_of_pizza = input("Please chose the pizza size... S or L or M")
add_peperonni = input("Would you like to add peperonni...? Y or N ")
extra_cheese = input("Do you want extra cheese..? Y or N")

if size_of_pizza == "S":
    Bill = 20
elif size_of_pizza == "M":
    Bill = 40
else: 
    Bill = 50

if add_peperonni == "Y":
    if size_of_pizza == "S":
        Bill += 2
    else:
        Bill += 3


    if extra_cheese == "Y":
        Bill += 1
   
print(f"Your final Bill is ${Bill}")    


