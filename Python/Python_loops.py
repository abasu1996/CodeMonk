import random
heights = input("Mention the heights of the students...").split(" ")
total_height = 0
for item in heights:
    total_height += int(item)

number_of_students = 0

for item2 in heights:
    number_of_students+=1
average_height = total_height / number_of_students    

print(f"Average height of the students is {average_height} ")


##Highest Score

list_down_scores = input("Please list down all the scores....!!").split(",")
for n in range(0,len(list_down_scores)):
    list_down_scores[n] = int(list_down_scores[n])
highest_score = 0
for score in list_down_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is...{highest_score}")

##Adding even numbers
total = 0
for number in range(0,100,2):
    total+=number
print(f"The total is {total}")

##FizzBuzz

range_number = 0

for n in range(1,101):

    if n % 5 == 0 and n % 3 == 0:
         print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


##Random Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

random.shuffle(letters)

c_numbers = int(input("How many numbers do you wanna keep?.. "))
c_letters = int(input("How many letters do you wanna keep?.. "))
c_symbols = int(input("How many symbols do you wanna keep?.. "))
password_list = []

for char in range(1, c_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, c_numbers+1):
    password_list.append(random.choice(numbers))
for char in range(1, c_symbols+1):
    password_list.append(random.choice(symbols))
print(password_list)

random.shuffle(password_list)

print(password_list)
password = ""
for char in password_list:
    password+= char
print(password)

def pypart(n):
    for each in range(0,n):
        for j in range(0,each+1):
            print("*", end=" ")
            
        print("\n")

n=10
pypart(n)


for number in range(0,11):
    for j in range(1, number+1):
        print(j,end="")
    
    print("\n")


list_1 = [10,20,30,40,50]
list_2 = reversed(list_1)

for i in list_2:
    print([i])



    


