name = input()
phone = input()
query_name = input()

pbook = {name: phone}

print(pbook.get(query_name, "NOTFOUND"))