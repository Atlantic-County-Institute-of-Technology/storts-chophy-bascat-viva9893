# author: Cesar

import os
import random

os.system('cls' if os.name == 'nt' else 'clear')

MAX_TRIES = 5
WORD_LIST = []
WORD_LEN = 5


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


if __name__ == '__main__':
    main()

