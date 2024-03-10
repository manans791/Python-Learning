a= int(input('Enter a number: '))


def fact(i):
    factorial = 1
    for i in range(1,11):
        factorial = i* factorial

    return factorial

print(fact(a))