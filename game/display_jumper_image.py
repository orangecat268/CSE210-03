class display_jumper_image:

    # Displays each image of jumper starting from
    # no misses to run out of turns

    def player_guess(guess=1):
        if guess == 1:
            print("_ _ _ _ _")
            print(" ")
            print("  ___")
            print(" /___\\")
            print(" \   / ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        elif guess == 2:
            print("_ _ _ _ _")
            print(" ")
            print(" /___\\")
            print(" \   / ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        elif guess == 3:
            print("_ _ _ _ _")
            print(" ")
            print(" \   / ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        elif guess == 4:
            print("_ _ _ _ _")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        elif guess == 5:
            print("_ _ _ _ _")
            print(" ")
            print("   x   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")
        else:
            print("_ _ _ _ _")
            print(" ")
            print("  ___")
            print(" /___\\")
            print(" \   / ")
            print("  \ / ")
            print("   O   ")
            print("  /|\\ ")
            print("  / \ ")
            print(" ")
            print("^^^^^^^")

    def play_screen_update(random_word, incorrect_guesses, hidden_word, eval_guess=0, LIMIT=5, game_status="2", last_tried=""):

        print()
        print("   __  _  _  _  _  ____  ____  ____ ")
        print(" _(  ) / )((/ )(  _ \(  __)(  _ \\")
        print("/ \) \) \/ (/ \/ \ ) __/ ) _)  )   /")
        print("\____/\____/\_)(_/(__)  (____)(__\_)")
        print()

        display_jumper_image.player_guess(len(incorrect_guesses))

        if game_status == 0:
            print(f"Game Over - the word was: {random_word} \n")
            print(f"Incorrect guesses: {incorrect_guesses} \n")
        elif game_status == 1:
            print(f"WOOOOOHOOOOOOOO")
            print(f"YOU WIN - the word was: {random_word} \n")
            print(f"Incorrect guesses: {incorrect_guesses} \n")
        else:
            print(f"\nYour hidden word looks like this: {hidden_word}")
            if len(incorrect_guesses) > 0:
                print(
                    f"Incorrect guesses: '{incorrect_guesses}'")
            elif len(incorrect_guesses) > 1:
                print(
                    f"Incorrect guesses: '{incorrect_guesses}'")

            guesses_left = 0
            guesses_left = 5 - int(len(incorrect_guesses))
            print(f"{guesses_left} remaining guesses \n")
