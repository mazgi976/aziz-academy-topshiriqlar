brand = input().strip()
year_input = input().strip()

try:
    year = int(year_input)
    if brand and 1886 <= year <= 2100:
        print(f"CAR={brand} YEAR={year}")
    else:
        print("BAD")
except ValueError:
    print("BAD")