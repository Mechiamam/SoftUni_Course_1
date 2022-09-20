year = int(input("Enter your chosen year: "))


def is_ascending(lst):
    return sorted(lst) == lst


distinct_digits = False
while not distinct_digits:
    if year_list[0] != year_list[1] and year_list[0] != year_list[4] and year_list[0] != year_list[3] \
            and year_list[0] != year_list[2]:
        distinct_digits = True
        print(year_list)
        break
    year += 1
    year_list = [int(year) for i in str(year)]

# You are saying goodbye to your best friend:
# "See you next happy year". Happy Year is the year with only distinct digits,
# for example, 2018. Write a program that receives an integer number and finds the next happy year.

# TODO
