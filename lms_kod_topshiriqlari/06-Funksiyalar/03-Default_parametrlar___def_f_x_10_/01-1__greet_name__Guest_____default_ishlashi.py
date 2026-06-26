def greet(name='Guest'):
    return f"Hello, {name}!"

input_data = input().strip()

if input_data:
    print(greet(input_data))
else:
    print(greet())