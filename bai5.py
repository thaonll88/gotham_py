def print_num():
    num = int(raw_input("Please enter a float number equal or larger than zero: "))
    if num < 0:
        print "This number has to be equal or larger than zero"
    elif num == 0:
        print "factorial of", num, "is", 1
    elif num == 1:
        print "factorial of", num, "is", 1
    else:
        print "factorial of", num, "is", factorial(num)

def factorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial = factorial * i
    return factorial

print_num()