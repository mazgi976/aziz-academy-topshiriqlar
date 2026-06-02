def make_user(name, role='student'):
    return f"name={name}, role={role}"

tokens = input().split()

if len(tokens) == 1:
    print(make_user(tokens[0]))
else:
    print(make_user(tokens[0], tokens[1]))