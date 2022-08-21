import string
import random
from typing import List
from abc import ABC, abstractmethod
import os

# class IGenerator(ABC):
#     @abstractmethod
#     def generate(self, words: List[string]) -> string:
#         pass

# class RandomGenerator(IGenerator):
#     def generate(self, words: List[string]) -> string:
#         return list.copy()

# class SortedGenerator(IGenerator):
#     def generate(self, words: List[string]) -> string:
#         list_copy = list.copy()
#         list_copy.reverse()
#         return list_copy

# class OrderedGenerator(IGenerator):
#     def generate(self, words: List[string]) -> string:
#         list_copy = list.copy()
#         random.shuffle(list_copy)
#         return list_copy

# class IWordAdder(ABC):
#     @abstractmethod
#     def add_word(self, word: string) -> string:
#         pass

# class LowercaseWordAdder(IWordAdder):
#     def add_word(self, word: string) -> string:
#         return word.lower()

# class UppercaseReverseWordAdder(IWordAdder):
#     def add_word(self, word: string) -> string:
#         return word.upper()

# class SentenceGenerator:

#     def generate(self, generator: IGenerator):
#         return generator.generate()

#     def add_word(self, word_adder: IWordAdder):
#         return word_adder.add_word()

class SentenceGeneratorApplication:

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

    def __init__(self):
        self.menu_state = self.generator_menu_state
        self.menu_title = self.generator_menu_title
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
            self.action_menu_title = menu[choice]
            self.change_menu_state()
        elif self.menu_state == 0 and choice == 2:
            self.action_menu_title = menu[choice]
            self.change_menu_state()
        elif self.menu_state == 0 and choice == 3:
            self.action_menu_title = menu[choice]
            self.change_menu_state()
        elif self.menu_state == 0 and choice == 4:
            exit()

        # Action Menu

        elif self.menu_state == 1 and choice == 1:
            print(menu[choice])
            
        elif self.menu_state == 1 and choice == 2:
            print(menu[choice])
            
        elif self.menu_state == 1 and choice == 3:
            print(menu[choice])
            
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