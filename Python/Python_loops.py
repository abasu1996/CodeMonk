
heights = input("Mention the heights of the students...").split(" ")
total_height = 0
for item in heights:
    total_height += int(item)

number_of_strudents = 0

for item2 in heights:
    number_of_strudents+=1
average_height = total_height / number_of_strudents    

print(f"Average height of the students is {average_height} ")