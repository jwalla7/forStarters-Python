from timeit import default_timer as runtime_timer

# Strings: ordered, immutable, text representation


print("------ example 1 ------")
name_string = input('Please enter your name:')

single_line_string = 'Hello'

double_line_string = """Line 1 \
Line 2
Line 3 
Line 4"""

substring_el = single_line_string[1:3]
substring_he = single_line_string[:2]
substring_reversed = single_line_string[::-1]


print('Nice to meet you,', name_string + '.')  # The " , " concatenates and adds a space. The " + " concatenates only
print(single_line_string)
print(double_line_string)
print(substring_el)
print(substring_he)
print(substring_reversed)

print("------ example 2 ------")
a = "Joseph"
sentence = "Hello my name is %s" % a
print(sentence)

a_1 = "James"
sentence_0 = "Hello my name is {1}, {0} {1}".format(a, a_1)
print(sentence_0)


print("------ example 3 ------")
b = 3.1234567
floating_number_0 = "the floating number is %.2f" % b
print(floating_number_0)

c = 2.1234567
floating_number_1 = "the floating number is {}".format(c)
print(floating_number_1)

d = 1.1234567
e = 7
floating_number_2 = "the floating number is {:.2f} and {}".format(d, e)
print(floating_number_2)

# faster runtime option (formatted string)
f = 4.1234567
g = 3
floating_number_3 = f"the floating number is {f:.2f} and {g * f}"
print(floating_number_3)

print("------ example 4 ------")
greeting = "Hello World  "

if "o" in greeting:
    print(greeting)
else:
    print("Goodbye")

greeting_no_whitespaces = greeting.strip()
greeting_uppercase = greeting.upper()  # HELLO WORLD
greeting_starts_with = greeting.startswith("a")  # False
greeting_replace_word = greeting.replace("World", "Universe")  # Hello Universe
greeting_isolate_each_word_by_delimiter = greeting.split(" ")  # ['Hello', 'World', '', '']

print(greeting_no_whitespaces)
print(greeting_uppercase)
print(greeting_starts_with)
print(greeting_replace_word)
print(greeting_isolate_each_word_by_delimiter)


print("------ example 5 ------")
csv_example = "first_name,last_name,age"
csv_isolate_each_word_by_delimiter = csv_example.split(",")  # ['first_name', 'last_name', 'age']
csv_combine_each_word_by_delimiter = "".join(csv_isolate_each_word_by_delimiter)

print(csv_isolate_each_word_by_delimiter)
print(csv_combine_each_word_by_delimiter)

print("------ example 6 ------")
string_list = ["jx7"] * 7
print(string_list)

# test case 1: slower code
start_0 = runtime_timer()
j_string_0 = ""
for j in string_list:
    j_string_0 += j
print(j_string_0)
stop_0 = runtime_timer()
print("bad practice code j_string: " + str(stop_0 - start_0))

# test case 1: faster refactored code
start_1 = runtime_timer()
j_string_1 = ''.join(string_list)
print(j_string_1)
stop_1 = runtime_timer()
print("refactored j_string: " + str(stop_1 - start_1))


