s = input()
harflar = [f"'{i}'" for i in s]
natija = "{" + ", ".join(harflar) + "}"
print(natija)