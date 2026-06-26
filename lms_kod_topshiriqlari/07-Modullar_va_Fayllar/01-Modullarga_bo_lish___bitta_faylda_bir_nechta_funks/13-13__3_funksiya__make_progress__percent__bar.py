def percent(done, total):
    return (done * 100) // total

def bar(p):
    hashes = p // 10
    dots = 10 - hashes
    return "%" * hashes + "." * dots
    
def make_progress(done, total):
    p = percent(done, total)
    return f"{p}% {bar(p)}"
        
done, total = map(int, input().split())
print(make_progress(done, total))