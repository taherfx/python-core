a = ["apple", "banana", "cherry"]

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

len = len(a)
i = 0
while i < len:
    print(a[i])
    i += 1

[print(x) for x in a]

newlist = [x for x in a if 'a' in x]
print(newlist)