a = float(input('Enter a number: '))

def check(num):
    if num >= 1:
        print('Positive number')
    elif num == 0:
        print('Number is 0')
    else:
        print('Negative number')

check(a)