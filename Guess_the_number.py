import random

class MsgForGuess_number:

    def title_msg(self):
        return '+=+=+=+=+=+Угадай число+=+=+=+=+=+'

    def counter_msg(self):
        return (f'У вас {Guess_number.COUNTER} очков!')

    def input_number_msg(self):
        return 'Введите число: '

    def add_one_point(self):
        return 'Вы угадали. +1 Очко'

    def subtact_one_point(self):
        return 'Вы не угадали. -1 очко'

class Guess_number:
    COUNTER = 0
    def __init__(self):
        self.one_random_number = []
        self.msg = MsgForGuess_number()

    def main(self):
        print(self.msg.title_msg())
        while True:
            self.fill_number_list()
            print(f'У вас {self.COUNTER} очков!')
            self.check_number()
            self.game_over()
            self.clear_list()


    def fill_number_list(self):
        self.one_random_number.append(random.randint(0, 10))
        print(self.one_random_number)


    def check_number(self):
        #number = int(self.input_number())
        if int(self.input_number()) in self.one_random_number:
            print(self.msg.add_one_point())
            self.COUNTER = self.COUNTER + 1
        else:
            print(self.msg.subtact_one_point())
            self.COUNTER -= 1
    def input_number(self):
        number = input(self.msg.input_number_msg())
        return number

    def game_over(self):
        if self.COUNTER < 0:
            print('GameOver!')
            exit()
    def clear_list(self):
        self.one_random_number.clear()

game = Guess_number()
game.main()