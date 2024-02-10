def piramide_altura(base):
    for i in range(base):
        print(' ' * (base - i - 1) + '*' * (2 * i + 1))

def piramide_base(base):
    for i in range(base//2 + 1):
        print(' ' * (base//2 - i) + '*' * (2 * i + 1))

def rombo_lado(base):
    for i in range(base):
        print(' ' * (base - i - 1) + '*' * (2 * i + 1))
    for i in range(base-1 , -1, -1):
        print(' ' * (base - i) + '*' * (2 * i - 1))







if __name__ == '__main__':
    piramide_base(7)
    piramide_altura(3)
    rombo_lado(4)