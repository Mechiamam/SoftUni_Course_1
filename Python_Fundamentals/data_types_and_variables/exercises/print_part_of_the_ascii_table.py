starting_index = int(input())
final_index = int(input())
ascii_list = []
for i in range(starting_index, final_index + 1):
    ascii_list.append(chr(i))
print(' '.join(map(str, ascii_list)))