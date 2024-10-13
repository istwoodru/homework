def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    total = 0
    if len(str_number) < 1:
        return first
    else:
        total = first * get_multiplied_digits(int(str_number[1:]))
        return total


result = get_multiplied_digits(40203)
print(result)


