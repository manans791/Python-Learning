for i in range(1,21):
    if i % 3 ==0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    elif (i % 5 ==0) and (i % 3 ==0):
        print('Fizzbuzz')
    else:
        print(i)