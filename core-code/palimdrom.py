def _reversed(n):
    rev = 0
    temp = n
    while(temp != 0):
        ld = temp % 10
        rev = (rev * 10) + ld
        temp = temp // 10
    return (rev==n)

number = int(input("enter the number: "))
if _reversed(number):
    print("number is palimdrom")
else:
    print("number is not palimdrom")
