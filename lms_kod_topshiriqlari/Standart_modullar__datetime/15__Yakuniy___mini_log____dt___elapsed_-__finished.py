from datetime import datetime, timedelta

start_dt = datetime.fromisoformat(input().strip())
ops = int(input())
elapsed_ms = int(input())

elapsed_s = elapsed_ms / 1000
finish_dt = start_dt + timedelta(milliseconds=elapsed_ms)

if elapsed_s > 0:
    rate = ops / elapsed_s
else:
    rate = 0.0
    
start_str = start_dt.strftime('%Y-%m-%d %H:%M:%S')
finish_str = finish_dt.strftime('%Y-%m-%d %H:%M:%S')

print(f"start={start_str} finish={finish_str} rate={rate:.2f}")