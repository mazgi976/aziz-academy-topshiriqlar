import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0].strip())
    d = {}
    
    for i in range(1, n + 1):
        line = input_data[i].split()
        if len(line) >= 2:
            key = line[0]
            val = line[1]
            d[key] = val
    # Maslahatga muvofiq lug'atni kalit bo'yicha tartiblab chiqarish
    for k in sorted(d):
        print(k + "=" + d[k])
        
if __name__ == '__main__':
    solve()