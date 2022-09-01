thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

thisdict2 = {
  "brand": "Ford",
  "electric": (False, True),
  "year": {1964, 2020},
  "colors": ["red", "white", "blue"]
}

print(thisdict2)

print(thisdict2['year'])
print(thisdict2.get('colors'))
print(thisdict2.keys())
print(thisdict2.values())