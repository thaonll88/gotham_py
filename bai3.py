def numero_chequer(numero):
    numero = numero % 2
    if numero == 1:
        return "So le"
    elif numero == 0:
        return "So chan"


def main():
    numero = int(raw_input("please enter a number: "))
    print(numero_chequer(numero))


main()