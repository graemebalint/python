import random
import config

class generatePassword:

    def __init__(self):
        # print("Welcome to the PyPassword Generator!")
        # nr_letters = int(input("How many letters would you like in your password?\n"))
        # nr_symbols = int(input(f"How many symbols would you like?\n"))
        # nr_numbers = int(input(f"How many numbers would you like?\n"))

        # choice = 'y'
        #
        # while choice == 'y':
        self.nr_letters = 8
        self.nr_symbols = 2
        self.nr_numbers = 2

        self.password = ""
        self.password_length = self.nr_letters + self.nr_numbers + self.nr_symbols

        self.all_char = config.letters + config.numbers + config.symbols
        self.letter_count = self.nr_letters
        self.number_count = self.nr_numbers
        self.symbol_count = self.nr_symbols

        while len(self.password) < self.password_length:
            # generate random index number between 0 and the length of all_char
            index = random.randint(0, (len(self.all_char) - 1))
            if (config.letters.count(self.all_char[index]) == 1) and (self.letter_count > 0):
                self.password += self.all_char[index]
                self.letter_count -= 1
            elif (config.numbers.count(self.all_char[index]) == 1) and (self.number_count > 0):
                self.password += self.all_char[index]
                self.number_count -= 1
            elif (config.symbols.count(self.all_char[index]) == 1) and (self.symbol_count > 0):
                new_index = random.randint(0, (len(config.symbols) - 1))
                self.password += config.symbols[new_index]
                self.symbol_count -= 1
            else:
                continue
                #pass

    def return_password(self):
        return self.password
        # print(f"Password: {password}")
        # choice = input("Would you like to generate another password? ")
