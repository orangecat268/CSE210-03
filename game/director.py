
import os
from game.display_jumper_image import display_jumper_image
from game.get_random_word import get_random_word
from game.play_Jumper_game import play_Jumper_Game
from game.read_Jumper_words import read_Jumper_words


class Director:

    def __init__(self):
        game_play = ""
        Jumper_word_list = []
        dictionary_word_list = []
        Players_Name = ""
        random_word_nc = ""
        random_word = ""
        jumper_word = ""
        fastest_time = 0
        name_top_score = "peter"

    def start_game(self):

        #Players_Name = input("Please enter your Name : ")
        display_jumper_image.player_guess(1)
        #print(f"Welcome to JUMPER, {Players_Name} ")
        dictionary_word_list = read_Jumper_words.read_Jumper_words(
            "week3\Jumper\CSE210-03\jumper.csv", 0)
        # print(dictionary_word_list)
        self.random_word_nc = get_random_word.get_random_word(
            dictionary_word_list)
        # print(random_word_nc)
        self.random_word = self.random_word_nc.upper()
        self.jumper_word = ["#" for i in range(len(self.random_word))]
        # print(jumper_word)
        #new_record_guesses = play_Jumper_Game.play_Jumper_Game(self.random_word, self.fastest_time, self.name_top_score, "", self.jumper_word, 0, 5, "", "")
        new_record_guesses = play_Jumper_Game.play_Jumper_Game(
            self.random_word, 0, 0, "", self.jumper_word, 0, 5, "", "")

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
