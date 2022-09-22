first_int = int(input())
second_int = int(input())
list_int = [first_int, second_int]
print(f"Before:\n a = {first_int}\n b = {second_int}")
first_int = list_int[1]
second_int = list_int[0]
print(f"After:\n a = {first_int}\n b = {second_int}\n")


