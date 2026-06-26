try:
    n = int(input())
    lst = [input() for _ in range(n)]
    idx = input()
    print(lst[int(idx)])
except IndexError:
    print("OUT")
except (ValueError, TypeError):
    print("TYPE")