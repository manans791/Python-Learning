a = int(input('Enter a number: '))

def year(num):
    if (num %400 ==0) or (num % 4 ==0 and num % 100 !=0):
        print(num,'Year is leap')
    else:
        print(num,'Year is not leap')


year(a)