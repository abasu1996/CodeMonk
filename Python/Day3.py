his_name = input("What is HIS Name...? ")
her_name = input("What is HER Name...? ")
combined_string1 = his_name + her_name
combined_string = combined_string1.lower()
T = combined_string.count('t')
R = combined_string.count('r')
U = combined_string.count('u')
E = combined_string.count('e')
L = combined_string.count('l')
O = combined_string.count('o')
V = combined_string.count('v')
E = combined_string.count('e')


true = T+R+U+E
love = L+O+V+E
love_score = int(str(true) + str(love))


if love_score < 20 and love_score > 40:
    print(f"Your Score is {love_score} and You are like coke and mentos")
else:
    print(f"Your score is {love_score} and You guys are perfect")
