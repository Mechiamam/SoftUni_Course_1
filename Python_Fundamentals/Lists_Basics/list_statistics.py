number_of_lines = int(input())
list_of_positives = []
list_of_negatives = []
positive_counter = 0
sum_of_negatives = 0
for i in range(1, number_of_lines + 1):
    integer = int(input())
    if integer < 0:
        list_of_negatives.append(integer)
        sum_of_negatives += integer
    else:
        list_of_positives.append(integer)
        positive_counter += 1
print(list_of_positives)
print(list_of_negatives)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {sum_of_negatives}")
