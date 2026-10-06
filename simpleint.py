import sys
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    number=int(sys.argv[1])
    print("Even and odd ",check_even_odd(number))