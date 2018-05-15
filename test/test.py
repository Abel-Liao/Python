a = 9
def test():
    global a
    a = 10
    print(a)
    def test1():
        nonlocal a
        a = 11
        print(a)
    test1()
test()
print(a)