import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return
    
    a = input_data[0].split()
    b = input_data[1].split()
    
    # Maslahatga muvofiq birinchi ro'yxatda bor, ikkinchisida yo'qlarini topib tartiblash
    result = sorted(set(a) - set(b))
    
    print(*result)
    
if __name__ == '__main__':
    solve()