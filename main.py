# author: Cesar

import os
import random

os.system('cls' if os.name == 'nt' else 'clear')


WORD_LIST = []




def extract_words():



    try:
        with open("assets/words_alpha.txt", "r") as file:
            for word in file.readlines():
                if len(word.strip()) == WORD_LEN:
                    WORD_LIST.append(word.strip())
        # Choose target word from the list
        return random.choice(WORD_LIST)
    except FileNotFoundError:
        print("File not found: assets/words_alpha.txt")
        return None


def main():

    # game dificulity
    MAX_TRIES = 5
    WORD_LEN = 5
    while True:
        print("[-]  0. Exit Site\n"
              f"[-] 1. Generate A {WORD_LEN} letter word \n"
              f"[-] 2. Change Difficulty \n")
        try:
            selection = int(input("Please select an option (0-1): "))
        except ValueError:
            print("(Invalid input")

        if selection == 0:
            print("Program is existing")
            exit()
        elif selection == 1:
            target = extract_words()
            if not target:
                return  # stop if file not found
            tries = 0
            while tries < MAX_TRIES:
                guess = input(f"Attempt {tries + 1}/{MAX_TRIES} — Enter a {WORD_LEN}-letter word: ").lower().strip()

                if len(guess) != WORD_LEN:
                    print(f"Word must be {WORD_LEN} letters long.")
                    continue

                if guess == target:
                    print("Correct! You guessed the word.")
                    break

                # Compare letters
                response = ["Bascat"] * WORD_LEN  # default feedback
                for i in range(WORD_LEN):
                    if guess[i] == target[i]:
                        response[i] = "chophy"  # correct position
                    elif guess[i] in target:
                        response[i] = "storts"  # wrong position

                print(" ".join(response))
                tries += 1

            if tries == MAX_TRIES and guess != target:
                print(f" Out of tries. The word was '{target}'.")
        elif selection== 2:
           MAX_TRIES = int(input("how many tries will you like to have"))
           while True:
               try:
                    WORD_LEN = int(input("What will the new word length must be a LEN 4-8  :   "))
                    assert WORD_LEN > 3 and WORD_LEN < 9
                    break
               except AssertionError:
                   print("value not in range  ")





if __name__ == '__main__':
    main()
