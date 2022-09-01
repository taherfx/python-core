a = ['apple', 'banna', 'chiku', 'mango', 'graps']

print(a)
a[1] = 'Banna'
print(a)

a[1:3] = ['banna', 'Chiku']
print(a)

a.insert(4, 'watermelon')

print(a)

a.append('lichi')
print(a)

b = ['tomato', 'potato', 'began']

a.extend(b)
print(a)

tuplearr = ('kivi', 'orange')

a.extend(tuplearr)
print(a)