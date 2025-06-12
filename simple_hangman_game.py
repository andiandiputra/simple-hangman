import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

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

words = [
    "apel",
    "jeruk",
    "mangga",
    "pisang",
    "anggur",
    "semangka",
    "melon",
    "pepaya",
    "nanas",
    "stroberi",
    "durian",
    "rambutan",
    "salak",
    "jambu",
    "alpukat",
    "kiwi",
    "leci",
    "belimbing",
    "sirsak",
    "markisa",
    "duku",
    "manggis",
    "sawo",
    "kedondong",
    "ceri",
    "delima",
    "sukun",
    "kesemek",
    "langsat",
]

random_choice = random.choice(words)
blank_list = []
end_of_game = True
lives = 6

for char in range(len(random_choice)):
    blank_list += "-"

print(f"{logo}\n\n----WELCOME---\nThe clue is a fruit name in Bahasa")

while end_of_game :
    answer = input("Input a word to guess :").lower()

    if answer in blank_list:
        print(f"You've already used '{answer}' word")

    for position in range(len(random_choice)):
        letter = random_choice[position]
        if letter == answer:
            blank_list[position] = letter
    
    if answer not in random_choice:
        lives -= 1
        print("\n---Wrong Answer---")
       
    if lives == 0:
        print(f"\n---You lose---\nthe answer was {random_choice}")
        end_of_game = False
    
    print(stages[lives])
    print(blank_list)
    
    if "-" not in blank_list:
        print("You won, congrats!")
        end_of_game = False