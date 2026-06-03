n = int(input())

info_count = 0
warn_count = 0
error_count = 0

for _ in range(n):
    qator = input()
    level = qator.split(":")[0].strip()
    
    if level == "INFO":
        info_count += 1
    elif level == "WARN":
        warn_count += 1
    elif level == "ERROR":
        error_count += 1
        
print(f"INFO {info_count}")
print(f"WARN {warn_count}")
print(f"ERROR {error_count}")