tank_capacity = 255
total_fill = 0
number_of_lines = int(input())
for i in range(number_of_lines):
    liters_of_water = int(input())
    total_fill += liters_of_water
    if tank_capacity < total_fill:
        total_fill -= liters_of_water
        print("Insufficient capacity!")
        continue
print(total_fill)
