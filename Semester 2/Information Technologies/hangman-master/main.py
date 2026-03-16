import game

game.start_game()
while True:
    word = game.choose_random_word()
    status = game.game(word)
    print("Congratulations, you win!") if status else print(f"You lose. The correct word was: {word}")
    again = input("Do you want to play again? (y/n):").strip().lower()
    if again in ("y", "yes"):
        continue
    else:
        break
