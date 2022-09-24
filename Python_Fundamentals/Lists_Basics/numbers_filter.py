number_of_lines = int(input())
list_of_integers = []
filtered_list = []
for i in range(number_of_lines):
    integer = int(input())
    list_of_integers.append(integer)
command = input()
if command == "even":
    for number in list_of_integers:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == "odd":
    for number in list_of_integers:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == "negative":
    for number in list_of_integers:
        if number < 0:
            filtered_list.append(number)
elif command == "positive":
    for number in list_of_integers:
        if number >= 0:
            filtered_list.append(number)
print(filtered_list)
