"<3 === green\
 <4 === yellow\
 <5 === red"

GREEN = 3
YELLOW = 4
RED = 5

class Definer:
    def __init__(self, number):
        self.number = number

    def get_needed_data(self):
        return self.number % 5

    def define_the_color(self, number):
        if number < GREEN:
            return 'green'
        elif number >= GREEN and number < YELLOW:
            return 'yellow'
        elif number >= YELLOW and number < RED:
            return 'red'

    def execute(self):
        if self.number >= 0:
            return self.define_the_color(self.get_needed_data())
        return 'Number less then 0.'


if __name__ == '__main__':
    num = float(input('Input any num: '))
    print(Definer(num).execute())
