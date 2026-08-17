def tanishtir(ism, familiya, yosh):
    return f"{ism} {familiya}, {yosh} yosh"


ism = input().strip()
familiya = input().strip()
yosh = input().strip()

print(tanishtir(ism, familiya, yosh))