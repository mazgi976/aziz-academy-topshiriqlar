def power(a, b=2):
    return a ** b

input_data = input().split()

if len(input_data) == 1:
    print(power(int(input_data[0])))
else:
    print(power(int(input_data[0]), int(input_data[1])))