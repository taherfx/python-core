a = ("apple", "banana", "cherry")
b = list(a)
b[1] = "kiwi"
a = tuple(b)

print(a)