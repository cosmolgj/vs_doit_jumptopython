
# add dic 
a = {1: 'a'}
print("\na dictionary: {0}".format(a))

a[2] = 'b'
print("add a[2] = b: {0}".format(a))

a['name'] = 'pooh'
print("add a['name'] = 'pooh': {0}".format(a))

a[3] = [1, 2, 3]
print("add a[3] = [1, 2, 3]: {0}".format(a))


# delete dictionary 
del a[1]
print("\ndelete dictionary a[1]: {0}".format(a))


# keys
a = {'name': 'pooh', 'phone':'01093829472', 'birth':  '1125'}
print("\nlist a: {0}".format(a))
print("key list of dictionary a: {0}".format(a.keys()))
print("value list of dictionary a: {0}".format(a.values()))

for k in a.keys():
    print(k)

# items of dictionary

print("\nget items of dic a: \n{0}".format(a.items()))


# get value of dictionary
print("\nget value of name of dic_a: {0}".format(a.get('name')))


# delete all items of dictioniary
a.clear()
print("\ndelete all items: {0}".format(a))
