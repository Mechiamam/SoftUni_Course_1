animal_tail = input()
animal_body = input()
animal_head = input()
animal_list = [animal_tail, animal_body, animal_head]
animal_list[0], animal_list[2] = animal_list[2], animal_list[0]
print(animal_list)

