number_of_lines = int(input())
special_word = input()
list_of_strings = []
for i in range(number_of_lines):
    string = input()
    list_of_strings.append(string)
print(list_of_strings)
for i in range(len(list_of_strings) -1, -1, -1):
    element = list_of_strings[i]
    if special_word not in element:
        list_of_strings.remove(element)
print(list_of_strings)