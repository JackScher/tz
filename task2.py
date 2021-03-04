class Replacement:
    constants_dictionary = {
        'Ave': 'Avenue',
        'Ave.': 'Avenue',
        'St': 'Street',
        'St.': 'Street',
        'Str': 'Street',
        'Str.': 'Street'
    }

    exceptions_list = ['Ave Maria']

    def __init__(self, random_string):
        self.arr = []
        self.exception = None
        for exception in self.exceptions_list:
            if exception in random_string:
                self.exception = exception
        if self.exception:
            arr = random_string.split(self.exception)
            for string in arr:
                self.arr.append(string.split())
        else:
            self.arr = random_string.split()

    def checker(self, list):
        for index in range(0, len(list)):
            if list[index][-1] == ',':
                list[index] = self.service(list[index][:-1])
                list[index] += ','
            else:
                list[index] = self.service(list[index])
        return list

    def service(self, item):
        for key in self.constants_dictionary:
            if item == key:
                return self.constants_dictionary[key]
        return item

    def helper(self):
        result = ''
        for item in self.arr:
            result_arr = self.checker(item)
            if result:
                result += ' '.join(result_arr)
            else:
                result = ' '.join(result_arr)
                result += ' ' + self.exception + ' '
        return result

    def execute(self):
        for item in self.arr:
            if type(item) == list:
                return self.helper()
        return ' '.join(self.checker(self.arr))


if __name__ == '__main__':
    string = '555 Straight Stave Ave, San Francisco, CA 94104 ' \
             '9032 Flave Steep Str, San Francisco, CA 94104 ' \
             '444 Ave Maria Stairway Street, San Francisco, CA 94104'
    print(Replacement(string).execute())