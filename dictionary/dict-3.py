thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "blue",
  "test": "Test"
}

thisdict.pop('model')
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict['brand']
print(thisdict)
thisdict.clear()
print(thisdict)
