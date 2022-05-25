
import random


class get_random_word():

    def get_random_word(dictionary_word_list, top_score_id=1, top_name_id=2):

        random_line = random.choice(list(dictionary_word_list.values()))
        random_word = random_line[0]
        #name_top_score = random_line[top_name_id]
        #fastest_time = random_line[top_score_id]
        return random_word
        # return random_word, fastest_time, name_top_score
        # print(name_top_score)
        # print(fastest_time)
        # print(random_word)
