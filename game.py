# Write it in Command Prompt (search for cmd) before running the code - pip install termcolor

# Libraries
import random
from termcolor import colored

# Beginning
def print_menu():
    print(colored("The game has started", "blue"))
    print(colored("----------------------------------------------------------------------------", "blue"))
    print(colored("Write a 5 letter word and press enter", "blue"))

# Random word from the file
def random_word():
    fhand = open("c:/users/user/OneDrive/Рабочий Стол/PBL project/words(only5letters_eng).txt", "r")
    lines = []
    while True:
        line = fhand.readline().rstrip().split()
        if not line:
            break
        lines = lines + line
    fhand.close()
    return random.choice(lines)

# Main
print_menu()
text = ""
while text != "0":
    print("")
    word_list = random_word()
    for attempt in range (1, 7):
        guess = input().lower()
        for n in range (5):
            if guess[n] == word_list[n]:
                print(colored(f"  {guess[n]}", "green"), end="")
            elif guess[n] in word_list:
                print(colored(f"  {guess[n]}", "yellow"), end="")
            else:
                print(f"  {guess[n]}", end="")
        print("")
            
        if guess == word_list:
            if attempt == 1:
                print(colored(f"\nCongratulation! You win in {attempt} attempt!\n", "green"))
            else:
                print(colored(f"\nCongratulation! You win in {attempt} attempts!\n", "green"))
            break
        elif attempt == 6:
            print(colored(f"\nYou lost, the word was [{word_list}]\n", "red"))
    text = input(colored("Do you want to continue playing? If not type 0 to exit : ", "blue"))
print(colored("Thanks for playing! See you next time!", "blue"))
print(colored("----------------------------------------------------------------------------", "blue"))