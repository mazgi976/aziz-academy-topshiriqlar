try:
    op = input()
    assert op in ('ADD', 'SUB')
    print("OK")
except AssertionError:
    print("OPERR")