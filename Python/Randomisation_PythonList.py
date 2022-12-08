import random

user_input = random.randint(0,1)
if user_input == 0:
    print("Heads")
else:
    print("Tails")
##Item and List 

fruits = ['apple', 'jackfruit', 'pear']
print(fruits)
fruits.insert(0,'mango')
print(fruits)
length = len(fruits)
print(length)
##Bill Pay Randomisation

names = input("Give me the name which will pay separated with comma and space ")
names_item = names.split(", ")
who_will_pay2 = random.choice(names_item)
length1 = len(names_item)

who_will_pay = random.choice(names_item)
print(who_will_pay2 + " Will pay the bill")

name2 = random.randrange(90)
print(name2)

fruits = ['mango', 'banana', 'pear']
vegetables = ['spinach', 'kale', 'potatoes']

dirty_dozen = [fruits,vegetables]
print(dirty_dozen[0][2])
print(dirty_dozen[1])


row1 = ['😁','😁','😁']
row2 = ['😁','😁','😁']
row3 = ['😁','😁','😁']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
treasure_loc = input("where you want to put your treasure separated with space...? ")
location = treasure_loc.split(",")
print(location)
row = int(location[0])
col = int(location[1])
map[row-1][col-1] = '🥶'
print(f"{row1}\n{row2}\n{row3}")



