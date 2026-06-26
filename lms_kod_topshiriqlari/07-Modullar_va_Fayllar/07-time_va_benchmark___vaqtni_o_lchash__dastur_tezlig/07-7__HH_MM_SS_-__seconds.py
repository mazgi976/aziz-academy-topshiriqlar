vaqt_str = input().strip()
hh, mm, ss = map(int, vaqt_str.split(':'))

total = hh * 3600 + mm * 60 + ss
print(total)