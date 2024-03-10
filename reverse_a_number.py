a = int(input('Enter a number: '))

def reverse(i):
    reverse_str_num = str(i)[::-1]
    reverse_num = int(reverse_str_num)
    return reverse_num

print(reverse(a))

print(type(a))