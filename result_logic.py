import random


def spin(debug=False):
    spin_num = random.randint(1, 1000)
    if debug:
        print(spin_num)
    if spin_num == 1000:
        if debug:
            print("q")
        return 7
    elif spin_num > 995:
        if debug:
            print("w")
        return 6
    elif spin_num > 985:
        if debug:
            print("e")
        return 5
    elif spin_num > 975:
        if debug:
            print("r")
        return 4
    elif spin_num > 960:
        if debug:
            print("t")
        return 3
    elif spin_num > 935:
        if debug:
            print("y")
        return 2
    elif spin_num > 900:
        if debug:
            print("u")
        return 1
    elif spin_num < 900:
        if debug:
            print("i")

        return False
