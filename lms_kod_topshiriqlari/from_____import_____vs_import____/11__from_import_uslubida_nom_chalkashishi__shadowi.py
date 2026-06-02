def my_len(s):
    count = 0
    for _ in s:
        count += 1
    return count

ops = {'len': my_len}

def main():
    s = input()
    len_fn = ops['len']
    print(len_fn(s))
    
if __name__ == '__main__':
    main()