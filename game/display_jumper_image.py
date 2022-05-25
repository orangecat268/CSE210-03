
class display_jumper_image:

    def __init__(self):

        self.guess = 1

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
        # clear_screen()

        print()
        print("   __  _  _  _  _  ____  ____  ____ ")
        print(" _(  ) / )((/ )(  _ \(  __)(  _ \\")
        print("/ \) \) \/ (/ \/ \ ) __/ ) _)  )   /")
        print("\____/\____/\_)(_/(__)  (____)(__\_)")
        print()

        display_jumper_image.player_guess(len(incorrect_guesses))

        if game_status == 0:
            print()
            print(f"Game over!!! your word was : {random_word} ")
            print()
            print(f"Your incorrect guesses were : {incorrect_guesses}")
        elif game_status == 1:
            print()
            print(f"WOOOOOHOOOOOOOO")
            print(f"YOU WIN!, You correctly guessed: {random_word}")
            print()
            print(f"Your incorrect guesses were : {incorrect_guesses}")
        else:
            print()
            print(f"Your hidden word looks like this : {hidden_word}")
            if len(incorrect_guesses) > 0:
                print(
                    f"You have made the following guess '{incorrect_guesses}' which is incorrect .")
            elif len(incorrect_guesses) > 1:
                print(
                    f"You have made the following guesses '{incorrect_guesses}' which are incorrect .")

            guesses_left = 0
            guesses_left = 5 - int(len(incorrect_guesses))
            # guesses_left_str = str(guesses_left)
            print(f"You have {guesses_left} incorrect guesses left.")
            # print(f"Length: {len(hidden_word)} last letter tried: {last_tried}")
            print()
            # return guesses_left
