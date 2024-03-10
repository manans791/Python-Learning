a=float(input('Enter a number: '))
b=float(input('Enter a number: '))

def add(num1,num2):
    if (a> 0) and (b>0):
        return int(a+b)

def mul(num1,num2):
    if (a> 0) and (b>0):
        return int(a*b)


print('Addition of two numbers: ',add(a,b))
print('Multiplication of two numbers: ',mul(a,b))