class Replacement:
    constants_dictionary = {
        'Ave': 'Avenue',
        'Ave.': 'Avenue',
        'St': 'Street',
        'St.': 'Street',
        'Str': 'Street',
        'Str.': 'Street'
    }

    def __init__(self, random_string):
        self.arr = random_string.split()

    def checker(self):
        for index in range(0, len(self.arr)):
            if self.arr[index][-1] == ',':
                self.arr[index] = self.service(self.arr[index][:-1])
                self.arr[index] += ','
            else:
                self.arr[index] = self.service(self.arr[index])
        return self.arr

    def service(self, item):
        for key in self.constants_dictionary:
            if item == key:
                return self.constants_dictionary[key]
        return item

    def execute(self):
        return ' '.join(self.checker())


if __name__ == '__main__':
    string = '555 Straight Stave Ave, San Francisco, CA 94104 ' \
             '444 Ave Maria Stairway St., San Francisco, CA 94104 ' \
             '9032 Flave Steep Str, San Francisco, CA 94104'
    print(Replacement(string).execute())