def age_getter():
    print("How old are ya?")
    try:
        age = int(input())
        print("You will be " + str(int(age) + 1) + " in a year")
    except ValueError:
        print("Age is a number mate, try again!")
        age_getter()


def check_uppercase(string):
    if string.islower():
        return False
    return True


def name_getter():
    print("What's your name?")
    name = input()
    if name.isalpha() and name[0].isupper() and name[1:].islower():
        print("Nice to meet you " + name)
        name_length = len(name)
        print("Your name has " + str(name_length) + " characters")
    elif name[0].islower():  # Makes sure Name starts with a capital
        print("Names start with a capital")
        name_getter()
    elif check_uppercase(name[1:]) is True and name.isalpha():  # makes sure no capital letters after first letter
        print("Capital letters at the start only...")
        name_getter()
    else:  # makes sure there are no numbers/special characters in the name
        print("Letters only!")
        name_getter()


print("Hello World!")
name_getter()
age_getter()
print("Big Brother thanks you!")
