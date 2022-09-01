# 0 1 1 2 3 5 8 13 21 34

def _fibo(n):
    if n <= 1:
        return n
    else:
        return _fibo(n-1) + _fibo(n-2)

n_terms = int(input("enter number "))
# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(_fibo(i))