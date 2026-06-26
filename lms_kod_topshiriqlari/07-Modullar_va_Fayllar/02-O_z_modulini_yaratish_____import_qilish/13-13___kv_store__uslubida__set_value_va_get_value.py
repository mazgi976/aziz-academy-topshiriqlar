store = {}


def set_value(key: str, val: str) -> None:
    store[key] = val
    
    
def get_value(key: str, default: str = "NONE") -> str:
    return store.get(key, default)


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        command = input().split()
        if command[0] == "set":
            set_value(command[1], command[2])
        elif command[0] == "get":
            print(get_value(command[1]))