import sys


def recursion_func(max_num, num=1):
    print(num)
    if max_num == num:
        sys.exit()
    else:
        return recursion_func(max_num, num+1)


if __name__ == '__main__':
    num = int(input('Input max num: '))
    recursion_func(num)
