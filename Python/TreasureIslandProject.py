print("Welcome to Treasure Island")
user_movement = input("Where do you want to go..? Left or Rigt\n ").lower()
if user_movement == "left":
    swim_boat = input("You came to a river Do you want to Swim across or Use a Boat..?  Swim/Boat\n").lower()
    print("You reached to an Island")
    user_move = input("Where do you want to go..? Left or Rigt \n").lower()
    if user_move == "left":
        print("You came to a door..!! and the room is full of fire.. Game Over")
    else:
        print("you finally found the treasure..!! You Win")
else:
    print("You fell into a Hole...!! Game Over")    
