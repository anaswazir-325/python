dict1 = {"name": "Anas", "age": 18, "city": "Lahore"}
dict2 = {"age": 20, "country": "Pakistan"}

marge = dict1.copy()
marge.update(dict2)
print(marge)