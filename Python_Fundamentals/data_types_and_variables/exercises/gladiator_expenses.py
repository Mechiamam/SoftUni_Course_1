lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_break_counter = 0
sword_break_counter = 0
shield_break_counter = 0
armor_break_counter = 0
total_expenses = 0
for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        helmet_break_counter += 1
    if i % 3 == 0:
        sword_break_counter += 1
        if i % 2 == 0:
            shield_break_counter += 1
            if shield_break_counter % 2 == 0:
                armor_break_counter += 1
total_expenses += helmet_price * helmet_break_counter + sword_price * sword_break_counter \
    + shield_price * shield_break_counter + armor_price * armor_break_counter
print(f"Gladiator expenses: {total_expenses:.2f} aureus")