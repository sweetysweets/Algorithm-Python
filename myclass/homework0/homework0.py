import sys


def problem1():

    for line in sys.stdin:
        arr = line.split(' ')
        result = int(arr[0]) + int(arr[1])
        print(result)

    # try:
    #     while True:
    #         s = input()
    #         s = s.split(' ')
    #         print(s)
    # except EOFError:
    #     pass


def problem2():
    for line in sys.stdin:
        arr = line.split(' ')
        result = int(arr[0]) + int(arr[1])
        print(result)


if __name__ == '__main__':
    problem2()

