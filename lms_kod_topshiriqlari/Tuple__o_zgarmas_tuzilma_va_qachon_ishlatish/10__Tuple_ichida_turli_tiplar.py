def parse_value(x):
    if x.isdigit():
        return int(x)
    try:
        return float(x) 
    except ValueError:
        return x

data = input().split()
t = tuple(parse_value(x) for x in data)

print(t)