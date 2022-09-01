x = lambda a, b : a + b

print(x(4,5))

def _fun(n):
    x = lambda a : a * n
    return x

myfn = _fun(21)
print(myfn(2))