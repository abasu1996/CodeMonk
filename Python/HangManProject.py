import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
words = ['apple','pear','banana','Jackfruit','Orange','Grapes']
random_word = random.choice(words)
display = []
for dash in range(len(random_word)):
    display+='_'
game_end = False

print(display)
while not game_end:
    Guess_Word = input("Guess The Letter: ").lower()

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == Guess_Word:
            display[position] = letter
    print(display)
    
    if Guess_Word not in random_word:
        lives -=1
        if lives == 0:
          game_end = True
          print("You Loose")
    
    print(f"{' '.join(display)}")
    if '_' not in display:
        game_end = True
        print("You Win")
    print(stages[lives])    
print(f"The Word is --> {random_word}")
    



