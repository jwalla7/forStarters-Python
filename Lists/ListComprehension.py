# Fast way to create a new list from an existing list

# Create a new list where values in "a" are squared
sequence_one = [1, 2, 3, 4, 5, 6]
sequence_one_squared = [i * i for i in sequence_one]

print("------ List Comprehension with int ------")
print("Sequence One List Values: " + str(sequence_one))

print("Sequence One List Values Squared: " + str(sequence_one_squared))
print()


print("------ List Comprehension with str ------")
first_names = ["Sogie", "Uzamere", "Osasumwen", "Ewaen", "Emwanta", "Bosa"]
first_names.sort()
last_names = ["Mama", "Orou", "Yacoubou", "Ibrahim", "Edah", "Togbe"]
last_names.sort()
full_names = [a + " " + i for a in first_names for i in last_names]
full_names.sort()

sorted_full_names_by_first_name = sorted(full_names, key=lambda n: n[0])
sorted_full_names_by_first_name_then_last_name = sorted(full_names, key=lambda n: n[0][0])
# sorted_full_names_by_first_name_reversed_then_last_name = sorted(full_names, key=lambda n: n[6::][0])




print("First Names: " + str(first_names))
print("Last Names: " + str(last_names))
print("Full Names: " + str(full_names))
print()

print("Sorted Names By First Names: " + str(sorted_full_names_by_first_name))
print("Sorted Names By First Then Last Names: " + str(sorted_full_names_by_first_name_then_last_name))
# print("Sorted Names By First Reversed Then Last Names: " + str(sorted_full_names_by_first_name_reversed_then_last_name))
