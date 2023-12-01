
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.


data = open('data.txt', 'r')
data = data.read().splitlines()

digit_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


total_sum = 0

for values in data:
    found_ints = []
    found_digits = {}
    for k, v in digit_mapping.items():

        for i in range(0, len(values)):
            if values[i:i+len(k)] == k:
                found_digits[i] = k
            if values[i] == str(v):
                found_digits[i] = str(v)

        # DOESNT WORK LOGIC
        # if k in values:
        #     index = values.index(k)
        #     found_digits[index] = k
        # if str(v) in values:
        #     index = values.index(str(v))
        #     found_digits[index] = str(v)

    sorted_dict = dict(sorted(found_digits.items()))
    print(sorted_dict)
    first = list(sorted_dict.values())[0]
    last = list(sorted_dict.values())[-1]
    if len(sorted_dict) > 0:
        if first in digit_mapping:
            first = digit_mapping[first]
        if last in digit_mapping:
            last = digit_mapping[last]

        total_sum += int(str(first) + str(last))

    print(first, last)
    print(values)

print(total_sum)
