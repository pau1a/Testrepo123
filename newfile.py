def ask_for_name():
    return input("What is your name? ")


def say_hi(name):
    print(f"hi {name}")


def say_hi_to_person():
    name = ask_for_name()
    say_hi(name)


say_hi_to_person()

