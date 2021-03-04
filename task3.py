"<3 === green\
 <4 === yellow\
 <5 === red"

color_dictionary = {
    'green': [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58],
    'yellow': [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59],
    'red': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
}


def define_the_color(num):
    if num < 0 or num > 60:
        return 'Wrong num!'
    for index in range(0, 12):
        if num < color_dictionary['green'][index]:
            return 'green'
        elif num >= color_dictionary['green'][index] and num < color_dictionary['yellow'][index]:
            return 'yellow'
        elif num >= color_dictionary['yellow'][index] and num < color_dictionary['red'][index]:
            return 'red'
        elif num == 60:
            return 'red'


if __name__ == '__main__':
    num = float(input('Input any num between 0 and 60: '))
    print(define_the_color(num))