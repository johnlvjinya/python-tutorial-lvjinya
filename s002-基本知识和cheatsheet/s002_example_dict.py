
mydict = {"a":30, "b":"我是帅哥", "list1":[2, 4, 5]}
print('mydict', mydict)

a = mydict.get("a")
print("a", a)

keys = mydict.keys()
print("keys", keys)

values = mydict.values()
print("values", values)

items = mydict.items()
print("items", items)


mydict2 = dict(zip(['fa', 'iii'], [55, [434, 554]]))
print("mydict2", mydict2)

mydict3 = {k for k, v in mydict.items() if v == [2,4,5]} 
print("mydict3", mydict3)

mydict4 = {k: v for k, v in mydict.items() if k in keys}
print("mydict4", mydict4)