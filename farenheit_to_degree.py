a = float(input('Enter a number: '))

def converter(num):
    celcius = (num-32) / 1.8

    return round(celcius,2)


print(converter(a))