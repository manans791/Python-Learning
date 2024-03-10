a = int(input('Enter a number: '))


def arm(num):
    str_num = str(num)
    total_digits = len(str_num)

    variable = 0
    for i in str_num:
        variable += int(i) ** total_digits
    return variable == num

if arm(a):
    print(a,' is Armstrong number')
else:
    print(a, ' is not Armstrong number')