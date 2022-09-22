number_of_lines = int(input())
opening_parentheses_counter = 0
expression = "BALANCED"
for i in range(1, number_of_lines + 1):
    user_input = input()
    if user_input == "(":
        if opening_parentheses_counter == 1:
            expression = "UNBALANCED"
        else:
            opening_parentheses_counter += 1
    elif user_input == ")":
        if opening_parentheses_counter == 0:
            expression = "UNBALANCED"
        else:
            opening_parentheses_counter = 0
    else:
        continue
print(expression)


