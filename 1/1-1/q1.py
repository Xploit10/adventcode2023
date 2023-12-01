# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# 12, 38, 15, and 77. Adding these together produces 142.


data = open('data.txt', 'r')
data = data.read().splitlines()
total_sum = 0
digits = [ord(str(digit)) for digit in range(0, 10)]

for values in data:
    found_ints = []
    for value in values:
        if ord(value) in digits:
            found_ints.append(value)
    total_sum += int(str(found_ints[0]) + str(found_ints[-1]))
