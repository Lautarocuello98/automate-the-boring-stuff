def a():
    print("a() start")
    b()
    d()
    print("a() end")
def b():
    print("b() start")
    c()
    print("b() end")
def c():
    print("c() start")
    print("c() end")
def d():
    print("d() start")
    print("d() end")

a()