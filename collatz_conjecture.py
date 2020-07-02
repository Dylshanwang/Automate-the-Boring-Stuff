counter = 1


def collatz(initial_number):
    global counter
    try:
        int_initial_number = int(initial_number)
        if int_initial_number % 2 == 0:
            even_number = int_initial_number / 2
            print(str(even_number))
            if even_number == 1:
                print("It took {} iterations to reach the number 1".format(counter))
            else:
                counter += 1
                collatz(even_number)
        else:
            odd_number = 3 * int_initial_number + 1
            print(str(odd_number))
            if odd_number == 1:
                print("It took {} iterations to reach the number 1".format(counter))
            else:
                counter += 1
                collatz(odd_number)
    except ValueError:
        number_getter()


def number_getter():
    print("Enter an integer")
    integer = input()
    collatz(integer)


number_getter()

