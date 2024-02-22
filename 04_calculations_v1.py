# convert to celsius
def to_celsius(to_convert):
    answer = (to_convert - 32) * 5 / 9
    return answer


# convert to fahrenheit
def to_fahrenheit(to_convert):
    answer = to_convert * 1.8 + 32
    return answer


# testing the components
to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    print("{} F os {:.0f} C".format(item, to_celsius(item)))
