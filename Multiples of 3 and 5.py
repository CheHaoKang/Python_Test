# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    multiplicands = [3, 5]
    multiplier = 1
    below_number = 1000
    qualified_numbers = set()

    while True:
        going = False
        for multiplicand in multiplicands:
            result = multiplicand * multiplier
            if result < below_number:
                going = True
                qualified_numbers.add(result)

        if going:
            multiplier += 1
        else:
            break

    # print(qualified_numbers)
    print(sum(qualified_numbers))