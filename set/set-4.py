x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

z = x.intersection(y)

print(x)
print(z)

x.symmetric_difference_update(y)
a = x.symmetric_difference(y)
print(x)
print(a)