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
    


