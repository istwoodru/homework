def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    last = int(str_number[-1])
    if len(str_number) < 2:
        return first
    if last == 0:
        str_number = str_number[:-1]
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return   first * get_multiplied_digits(int(str_number[1:]))
result = get_multiplied_digits(402030)
print(result)


