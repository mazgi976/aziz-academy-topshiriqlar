import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    total = 0
    
    idx = 1
    for _ in range(n):
        price = int(input_data[idx])
        quantity = int(input_data[idx+1])
        idx += 2
        
        item = {'narx': price, 'son': quantity}
        total += item['narx'] * item['son']
        
    print(total)
    
if __name__ == '__main__':
    solve()