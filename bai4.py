def print_num():
    num = int(raw_input("please enter a number: "))
    print(num_prime(num))

def num_prime(num):
    if num < 2:
            return "not prime"
    elif num == 2:
            return "is prime"
    else:
        for i in range(2,num):
            if num % i == 0:
                return "not prime"
        return "is prime"

print_num()