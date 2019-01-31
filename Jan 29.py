
y = 100

def f(x):

    x = x + y

    print("inside of f: " +str(x))
    return x


def g(x):

    f(x)
    print("f(x) returns: " +str(f(x)))
    print("inside of g: " +str(x))
    print(x)


print(y)
y = y + 100
print (y)

g(30)
