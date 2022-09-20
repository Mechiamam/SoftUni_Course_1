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

# if b[0] > b[1]:
#     print "Not ascending"

# TODO
