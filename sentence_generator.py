#-----------------------------------------------------
# fullname      :   s.m.mehrabul islam
# roll          :   sh-86
# email         :   smmehrabul-2017614964@cs.du.ac.bd
# institute     :   university of dhaka, bangladesh
# session       :   2017-2018
#-----------------------------------------------------

import string
import random
from typing import List
from abc import ABC, abstractmethod
from os import system, name

#-----------------------------------------------------

class IGenerator(ABC):
    @abstractmethod
    def generate(self, words):
        pass

class RandomGenerator(IGenerator):
    def generate(self, words):
        total_word_count = len(words)
        sentence_word_count = random.randint(1, total_word_count)
        
        word_count = 0
        sentence_words = []
        while word_count != sentence_word_count:
            # random
            index = random.randint(0, total_word_count-1)
            sentence_words.append(words[index])
            word_count += 1

        word_count = 0
        sentence = ""
        for sentence_word in sentence_words:
            if word_count != 0:
                sentence += " "
            sentence += sentence_word
            word_count += 1

        return sentence
        

class SortedGenerator(IGenerator):
    def generate(self, words):
        total_word_count = len(words)
        sentence_word_count = random.randint(1, total_word_count)
        
        word_count = 0
        sentence_words = []
        while word_count != sentence_word_count:
            index = random.randint(0, total_word_count-1)
            sentence_words.append(words[index])
            word_count += 1

        # sorting
        sentence_words.sort()

        word_count = 0
        sentence = ""
        for sentence_word in sentence_words:
            if word_count != 0:
                sentence += " "
            sentence += sentence_word
            word_count += 1

        return sentence

class OrderedGenerator(IGenerator):
    def generate(self, words):
        total_word_count = len(words)
        sentence_word_count = random.randint(1, total_word_count)
        
        word_index_count = 0
        sentence_word_indices = []
        while word_index_count != sentence_word_count:
            index = random.randint(0, total_word_count-1)
            sentence_word_indices.append(index)
            word_index_count += 1

        # ordering
        sentence_word_indices.sort()

        word_count = 0
        sentence = ""
        for sentence_word_index in sentence_word_indices:
            if word_count != 0:
                sentence += " "
            sentence += words[sentence_word_index]
            word_count += 1

        return sentence

#-----------------------------------------------------

class IWordModifier(ABC):
    @abstractmethod
    def get_modified_word(self, word):
        pass

class LowercaseWord(IWordModifier):
    def get_modified_word(self, word):
        word_lower = word.lower()
        return word_lower

class UppercaseReverseWord(IWordModifier):
    def get_modified_word(self, word):
        word_upper = word.upper()
        word_upper_reverse = word_upper[::-1]
        return word_upper_reverse

#-----------------------------------------------------

class SentenceGenerator:

    def __init__(self, words, generator: IGenerator, word_modifier: IWordModifier):
        self.generator = generator
        self.word_modifier = word_modifier
        self.words = words

    def generate(self):
        return self.generator.generate(self.words)

    def add_word(self, word):
        modified_word = self.word_modifier.get_modified_word(word)
        if modified_word in self.words:
            print(f"[DUPLICATE] {modified_word}")
        else:
            self.words.append(modified_word)
            print(f"[ADDED] {self.words[-1]}")
        return self.words

    def show_words(self):
        column_count = 5
        column_index = 0
        for word in self.words:
            print("{:<20}".format(word), end='')
            column_index = (column_index+1)%column_count
            if column_index == 0:
                print()
        if column_index != 0:
            print()

#-----------------------------------------------------

class SentenceGeneratorApplication:

    # menu variables

    MENU_OPTION_COUNT = 5
    MENU_OPTION_MIN = 0
    MENU_OPTION_MAX = 4

    generator_menu_state = 0
    generator_menu_title = 'Generators'
    generator_menu = {
        0: 'Refresh',
        1: 'Random Sentence Generator',
        2: 'Sorted Sentence Generator',
        3: 'Ordered Sentence Generator',
        4: 'Exit',
    }

    action_menu_state = 1
    action_menu = {
        0: 'Refresh',
        1: 'Generate Sentence',
        2: 'Add Word',
        3: 'Show Words',
        4: 'Back'
    }

    # word-sentence variables

    MIN_WORD_LENGTH = 1
    MAX_WORD_LENGTH = 18
    MAX_WORD_COUNT_IN_SENTENCE = 40

    wordsRSG = [
        "the", "at", "there", "some", "my",
        "of", "be", "use", "her", "than",
        "and", "this", "an", "would", "first",
        "a", "have", "each", "make", "water",
        "to", "from", "which", "like", "been",
        "in", "or", "she", "him", "call",
        "is", "one", "do", "into", "who",
        "you", "had", "how", "time", "oil",
        "that", "by", "their", "has", "its",
        "it", "word", "if", "look", "now",
        "he", "but", "will", "two", "find"
        "was", "not", "up", "more", "long",
        "for", "what", "other", "write", "down",
        "on", "all", "about", "go", "day",
        "are", "were", "out", "see", "did",
        "as", "we", "many", "number", "get",
        "with", "when", "then", "no", "come",
        "his", "your", "them", "way", "made",
        "they", "can", "these", "could", "may",
        "i", "said", "so", "people", "part"
    ]

    wordsSSG = [
        "the", "at", "there", "some", "my",
        "of", "be", "use", "her", "than",
        "and", "this", "an", "would", "first",
        "a", "have", "each", "make", "water",
        "to", "from", "which", "like", "been",
        "in", "or", "she", "him", "call",
        "is", "one", "do", "into", "who",
        "you", "had", "how", "time", "oil",
        "that", "by", "their", "has", "its",
        "it", "word", "if", "look", "now",
        "he", "but", "will", "two", "find"
        "was", "not", "up", "more", "long",
        "for", "what", "other", "write", "down",
        "on", "all", "about", "go", "day",
        "are", "were", "out", "see", "did",
        "as", "we", "many", "number", "get",
        "with", "when", "then", "no", "come",
        "his", "your", "them", "way", "made",
        "they", "can", "these", "could", "may",
        "i", "said", "so", "people", "part"
    ]

    wordsOSG = [
        "EHT", "TA", "EREHT", "EMOS",
        "YM", "FO", "EB", "ESU", "REH",
        "NAHT", "DNA", "SIHT", "NA", "DLUOW",
        "TSRIF", "A", "EVAH", "HCAE", "EKAM",
        "RETAW", "OT", "MORF", "HCIHW", "EKIL",
        "NEEB", "NI", "RO", "EHS", "MIH",
        "LLAC", "SI", "ENO", "OD", "OTNI",
        "OHW", "UOY", "DAH", "WOH", "EMIT",
        "LIO", "TAHT", "YB", "RIEHT", "SAH",
        "STI", "TI", "DROW", "FI", "KOOL",
        "WON", "EH", "TUB", "LLIW", "OWT",
        "SAWDNIF", "TON", "PU", "EROM", "GNOL",
        "ROF", "TAHW", "REHTO", "ETIRW", "NWOD",
        "NO", "LLA", "TUOBA", "OG", "YAD",
        "ERA", "EREW", "TUO", "EES", "DID",
        "SA", "EW", "YNAM", "REBMUN", "TEG",
        "HTIW", "NEHW", "NEHT", "ON", "EMOC",
        "SIH", "RUOY", "MEHT", "YAW", "EDAM",
        "YEHT", "NAC", "ESEHT", "DLUOC", "YAM",
        "I", "DIAS", "OS", "ELPOEP", "TRAP"
    ]

    # methods

    def __init__(self):
        self.menu_state = self.generator_menu_state
        self.menu_title = self.generator_menu_title
        self.sentence_generator = None
        pass

    def clear_console(self):
        # windows
        if name == 'nt':
            _ = system('cls')
        # linux/mac
        else:
            _ = system('clear')

    def print_menu(self):
        self.clear_console()
        
        menu = {}
        if self.menu_state == 0:
            menu = self.generator_menu
        elif self.menu_state == 1:
            menu = self.action_menu

        print("\n====================================")
        print(self.menu_title)
        print("====================================")

        for key in menu.keys():
            print (key, ':  ', menu[key])
        

    def handle_menu(self):
        choice = ''
        print()
        choice = input('> ')
        print()
        while not choice.isdigit():
            print(f"[INVALID] please enter a number between {MENU_OPTION_MIN} and {MENU_OPTION_MAX}, as the menu suggests")
            print()
            choice = input('> ')
            print()
        choice = int(choice)

        if choice > 4 or choice < 0:
            print(f"[INVALID] please enter a number between {MENU_OPTION_MIN} and {MENU_OPTION_MAX}, as the menu suggests")
        else:
            self.handle_options(choice)

    def handle_options(self, choice):

        menu = {}
        if self.menu_state == 0:
            menu = self.generator_menu
        elif self.menu_state == 1:
            menu = self.action_menu

        if choice == 0:
            self.refresh()
            return

        # generator menu
        
        if self.menu_state == 0 and choice == 1:
            self.sentence_generator = SentenceGenerator(self.wordsRSG, RandomGenerator(), LowercaseWord())
            self.action_menu_title = menu[choice]
            self.change_menu_state()
        elif self.menu_state == 0 and choice == 2:
            self.sentence_generator = SentenceGenerator(self.wordsSSG, SortedGenerator(), LowercaseWord())
            self.action_menu_title = menu[choice]
            self.change_menu_state()
        elif self.menu_state == 0 and choice == 3:
            self.sentence_generator = SentenceGenerator(self.wordsOSG, OrderedGenerator(), UppercaseReverseWord())
            self.action_menu_title = menu[choice]
            self.change_menu_state()
        elif self.menu_state == 0 and choice == 4:
            exit()

        # action menu

        elif self.menu_state == 1 and choice == 1:
            self.handle_generate_sentence()
        elif self.menu_state == 1 and choice == 2:
            self.handle_add_word()
        elif self.menu_state == 1 and choice == 3:
            self.handle_show_words()
        elif self.menu_state == 1 and choice == 4:
            self.sentence_generator = None
            self.change_menu_state()

    def change_menu_state(self):
        self.menu_state = 1-self.menu_state
        if self.menu_state == self.generator_menu_state:
            self.menu_title = self.generator_menu_title
        elif self.menu_state == self.action_menu_state:
            self.menu_title = self.action_menu_title

    def handle_generate_sentence(self):
        sentence = self.sentence_generator.generate()
        words = sentence.split(" ")

        print(f"[GENERATED] by {self.menu_title}")
        print("-----------------------------------------------")

        column_count = 10
        column_index = 0
        word_count = len(words)
        word_index = 0
        for word in words:
            word_index += 1
            if word_index == word_count:
                print(word, end=".")
            else:
                print(word, end=' ')
            column_index = (column_index+1)%column_count
            if column_index == 0:
                print()
        if column_index != 0:
            print("\n")

        print(f"Length      :   {len(sentence)}")
        print(f"Word Count  :   {len(words)}")

    def handle_add_word(self):
        entered_words = ''
        print("Enter Words: [if multiple words : separate using space]")
        print()
        entered_words = input('> ')
        print()

        entered_words = entered_words.split(" ")
        for entered_word in entered_words:
            if len(entered_word) < 1 or len(entered_word) > 18:
                print(f"[INVALID] couldn't add \"{entered_word}\"")
                print(f"[Note] word length must be between {self.MIN_WORD_LENGTH} and {self.MAX_WORD_LENGTH}.")
            if self.menu_title == "Random Sentence Generator":
                self.wordsRSG = self.sentence_generator.add_word(entered_word)
            elif self.menu_title == "Sorted Sentence Generator":
                self.wordsSSG = self.sentence_generator.add_word(entered_word)
            elif self.menu_title == "Ordered Sentence Generator":
                self.wordsOSG = self.sentence_generator.add_word(entered_word)
        print("[BACK TO MENU]")

    def handle_show_words(self):
        return self.sentence_generator.show_words()

    def refresh(self):
        self.menu_state = self.generator_menu_state
        self.menu_title = self.generator_menu_title
        self.sentence_generator = None
        self.launch()

    def launch(self):
        # menu loop
        previous_menu_state = -1
        while True:
            if self.menu_state != previous_menu_state:
                self.print_menu()            
            previous_menu_state = self.menu_state
            self.handle_menu()

#-----------------------------------------------------

if __name__=='__main__':
    app = SentenceGeneratorApplication()
    app.launch()