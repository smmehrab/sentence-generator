import string
import random
from typing import List
from abc import ABC, abstractmethod
import os

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

class SentenceGenerator:

    words = []

    def __init__(self, words, generator: IGenerator, word_modifier: IWordModifier):
        self.generator = generator
        self.word_modifier = word_modifier
        self.words = words

    def generate(self):
        return self.generator.generate(words)

    def add_word(self):
        modified_word = self.word_modifier.get_modified_word(word)
        words.append(modified_word)
        return words

    def show_words(self):
        print()
        column_count = 5
        column_index = 0
        for word in self.words:
            print("{:<20}".format(word), end='')
            column_index = (column_index+1)%column_count
            if column_index == 0:
                print()
        print()
            

class SentenceGeneratorApplication:

    # Menu Variables

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

    # Words

    wordsRSG = ["hellohellohello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"]
    wordsSSG = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"]
    wordsOSG = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"]

    # Methods

    def __init__(self):
        self.menu_state = self.generator_menu_state
        self.menu_title = self.generator_menu_title
        self.sentence_generator = None
        pass

    def print_menu(self):
        os.system("clear")
        
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
        print()

    def handle_menu(self):
        choice = ''
        try:
            choice = int(input('> '))
        except:
            print('[INVALID] please enter a number.')
        if choice > 4 or choice < 1:
            print('[INVALID] please enter a number between 1 and 4.')            
        else:
            self.handle_options(choice)

    def handle_options(self, choice):

        menu = {}
        if self.menu_state == 0:
            menu = self.generator_menu
        elif self.menu_state == 1:
            menu = self.action_menu

        # Generator Menu
        
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

        # Action Menu

        elif self.menu_state == 1 and choice == 1:
            print(menu[choice])
            
        elif self.menu_state == 1 and choice == 2:

            # self.sentence_generator.add_word(word)
            print(menu[choice])
            
        elif self.menu_state == 1 and choice == 3:
            self.sentence_generator.show_words()
            
        elif self.menu_state == 1 and choice == 4:
            # print(choice)
            self.change_menu_state()

    def change_menu_state(self):
            self.menu_state = 1-self.menu_state
            if self.menu_state == self.generator_menu_state:
                self.menu_title = self.generator_menu_title
            elif self.menu_state == self.action_menu_state:
                self.menu_title = self.action_menu_title

    def launch(self):
        # Menu Loop
        previous_menu_state = -1
        while True:
            if self.menu_state != previous_menu_state:
                self.print_menu()            
            previous_menu_state = self.menu_state
            self.handle_menu()

if __name__=='__main__':
    app = SentenceGeneratorApplication()
    app.launch()