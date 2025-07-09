import random
import data  
import os

def clear():
    os.system("cls")

def random_choice():
    fruit_data = random.choice(data.fruits)
    return fruit_data["name"].lower(), fruit_data["hint"]

def create_blank_list(fruit):
    return ["_"] * len(fruit)

def update_blanks(answer, fruit, blank_list):
    for position in range(len(fruit)):
        letter = fruit[position]
        if letter == answer:
            blank_list[position] = letter
    return blank_list

def play_game():
    while True:  
        clear()
        lives = 6
        fruit, hint = random_choice()
        blank_list = create_blank_list(fruit)
        guessed_letters = set()
        print(data.logo)
        print(f"Hint: {hint}")
        while lives > 0:
            print("\n" + " ".join(blank_list))
            print(data.stages[lives])
            answer = input("Guess a letter: ").lower()
            if len(answer) != 1 or not answer.isalpha():
                print("Please enter a single letter!")
                continue
            if answer in guessed_letters:
                print(f"You've already guessed '{answer}'")
                continue
            guessed_letters.add(answer)
            if answer in fruit:
                blank_list = update_blanks(answer, fruit, blank_list)
                if "_" not in blank_list:
                    print(f"\nCongratulations! You won! The fruit was '{fruit}'")
                    break
            else:
                lives -= 1
                print(f"\nWrong guess! You have {lives} lives remaining.")

        if lives == 0:
            print(f"\nGame Over! The fruit was '{fruit}'")
        play_again = input("\nPlay again? (Y/N): ").lower()
        if play_again != "y":
            print("GGWP!")
            break

play_game()