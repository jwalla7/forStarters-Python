even_num = [2, 4, 6, 8]
print(even_num)

double_even_num = map(lambda x_num: x_num + x_num, even_num)
print(list(double_even_num))

lowercase_string = ['hello', 'world']
uppercase_string = map(lambda lowercase_x: str.upper(lowercase_x), lowercase_string)
capitalize_string = map(lambda lowercase_j: str.capitalize(lowercase_j), lowercase_string)
print(list(lowercase_string))
print(list(uppercase_string))
print(list(capitalize_string))


