def print_number():
    numero = int(raw_input("please enter a number: "))
    print(numero_prime(numero))

def numero_prime(numero):
    if numero < 2:
            return "not prime"
    elif numero == 2:
            return "is prime"
    else:
        numero > 2;
        for i in range(2,numero):
            if numero % i == 0:
                return "not prime"
            else:
                return "is prime"

print_number()