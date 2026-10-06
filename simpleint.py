#simple intreset
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
if __name__ == "__main__":
    principal = 1000.00
    rate = 1.0
    time = 2.0
    interest = simple_interest(principal, rate, time)
    print(f"The simple interest is: {interest}")