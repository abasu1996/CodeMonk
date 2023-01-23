import random
from HangMan_Words import word_list
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

random_word = random.choice(word_list)
display = []
for dash in range(len(random_word)):
    display+='_'
game_end = False

print(display)
print(random_word)
while not game_end:
    Guess_Word = input("Guess The Letter: ").lower()

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == Guess_Word:
            display[position] = letter
            if Guess_Word in display:
              print("You already chose this word..!!")
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
    



