def count_pins(rows):
    amount = 0
    for row in range(1, rows + 1):
        amount += row
    print(amount)


count_pins(5)


# recursion
def sum_row(row):
    if row == 1:
        return 1
    else:
        return sum_row(row - 1) + row  # using the function


print(sum_row(100))


