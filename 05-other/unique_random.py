from random import randrange


def get_random_int():
    return randrange(10000)

def is_prime(num):
    for i in reversed(range(2, num)):
        if num%i==0:
            return False
    return True


mul = 1
index = 1
for i in range(1000):
    rand = get_random_int()
    if(is_prime(rand)):
        if(mul % rand != 0):
            print(f"{index}- num: {rand} mul: {mul}")
            mul *= rand
            index += 1

