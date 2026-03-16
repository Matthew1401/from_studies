import random
import hangman_steps as hs

MAX_MISTAKES = 7

def start_game():
    intro = r"""
      _   _                                         
     | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     |  _  | (_| | | | | (_| | | | | | | (_| | | | |
     |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        |___/                       
                        """

    print(intro)
    print("Welcome in the game of hangman, here you can check your knowledge of english vocabulary, "
          "you can have only 7 mistakes. Good luck!")
    input("Click enter to start...")
    print()


def game(word: str) -> bool:
    mistakes = 0
    guess = ["_" for _ in word]
    correct = list(word)
    guessed_letters = set()

    while True:
        if mistakes == MAX_MISTAKES:
            return False

        if "_" not in guess:
            return True

        print(f"\n{' '.join(guess)}     Mistakes: {mistakes}/{MAX_MISTAKES}\n{hs.hangman_steps[mistakes]}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        user = input("Input a letter: ").lower()
        if not (user.isalpha() and len(user) == 1):
            print("You must enter only ONE letter (a-z). Try again.")
            continue
        if user in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(user)

        if user in correct:
            for i, letter in enumerate(correct):
                if letter == user:
                    guess[i] = user
        else:
            mistakes += 1


def choose_random_word() -> str:
    file_name = "random_words.txt"
    try:
        with open(file_name, "r") as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found!")
        return "hangman"  # Default word so the game doesn't crash

    if not words:
        raise ValueError(f"Word list is empty! Please add words to '{file_name}'.")
    return random.choice(words)
