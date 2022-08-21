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
        pass

class SortedGenerator(IGenerator):
    def generate(self, words):
        pass

class OrderedGenerator(IGenerator):
    def generate(self, words):
        pass

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
        return self.generator.generate(words)

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

    generator_menu_state = 0
    generator_menu_title = 'Generators'
    generator_menu = {
        1: 'Random Sentence Generator',
        2: 'Sorted Sentence Generator',
        3: 'Ordered Sentence Generator',
        4: 'Exit',
    }

    action_menu_state = 1
    action_menu = {
        1: 'Generate Sentence',
        2: 'Add Word',
        3: 'Show Words',
        4: 'Back'
    }

    # word related variables

    MIN_WORD_LENGTH = 1
    MAX_WORD_LENGTH = 18

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
        "I", "said", "so", "people", "part"
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
        "I", "said", "so", "people", "part"
    ]

    wordsOSG = [
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
        "I", "said", "so", "people", "part"
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
            print('[INVALID] please enter a number between 1 and 4, as the menu suggests')
            print()
            choice = input('> ')
            print()
        choice = int(choice)

        if choice > 4 or choice < 1:
            print('[INVALID] please enter a number between 1 and 4, as the menu suggests')            
        else:
            self.handle_options(choice)

    def handle_options(self, choice):

        menu = {}
        if self.menu_state == 0:
            menu = self.generator_menu
        elif self.menu_state == 1:
            menu = self.action_menu

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
            print(menu[choice])
        elif self.menu_state == 1 and choice == 2:
            self.handle_word_input()
        elif self.menu_state == 1 and choice == 3:
            self.sentence_generator.show_words()
        elif self.menu_state == 1 and choice == 4:
            self.sentence_generator = None
            self.change_menu_state()

    def change_menu_state(self):
        self.menu_state = 1-self.menu_state
        if self.menu_state == self.generator_menu_state:
            self.menu_title = self.generator_menu_title
        elif self.menu_state == self.action_menu_state:
            self.menu_title = self.action_menu_title

    def handle_word_input(self):
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