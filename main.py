def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
print(get_multiplied_digits(2222))
print(get_multiplied_digits(322))
print(get_multiplied_digits(7))
