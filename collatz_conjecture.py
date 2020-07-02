counter = 0


def number_getter():
    print("Enter an integer")
    integer = input()
    collatz(integer)


def collatz(initial_number):
    global counter
    try:
        number = int(initial_number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(str(number))
                counter += 1
            else:
                number = 3 * number + 1
                print(str(number))
                counter += 1
        else:
            print("It took {} iterations to reach the number 1".format(counter))
    except ValueError:
        number_getter()


number_getter()
