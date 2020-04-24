def hw_week13(number):
    try:
        number = int(number)
    except ValueError:
        print('Please enter an positive integer.')
        return False

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = number * 3 + 1
        print(number)


if __name__ == '__main__':
    hw_week13(input('Please input the positive integer: '))
