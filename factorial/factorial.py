# 5! = 5*4*3*2*1 = 120

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

def Recur_facto(n, a = 1):
   
    if (n == 0):
        return a
   
    return Recur_facto(n - 1, n * a)
   
# print the result
print(Recur_facto(6))