number_of_snowballs = int(input())
highest_calc_value = 0
max_snowball_weight = 0
max_time_needed = 0
max_quality = 0
for i in range(number_of_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_calc_value = (snowball_weight / time_needed) ** quality
    if highest_calc_value < current_calc_value:
        highest_calc_value = current_calc_value
        max_snowball_weight = snowball_weight
        max_time_needed = time_needed
        max_quality = quality
print(f"{max_snowball_weight} : {max_time_needed} = {int(highest_calc_value)} ({max_quality})")

