def toliq_ism(ism, familiya):
    return f"{ism} {familiya}"


ism = input().strip()
familiya = input().strip()

print(toliq_ism(ism, familiya))