def to_seconds(h: int, m: int, s: int) -> int:
    return h * 3600 + m * 60 + s


def to_hms(total: int) -> tuple[int, int, int]:
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return h, m, s


if __name__ == "__main__":
    h, m, s = map(int, input().split())
    
    total_sec = to_seconds(h, m, s)
    print(total_sec)
    
    rh, rm, rs = to_hms(total_sec)
    print(f"{rh} {rm} {rs}")