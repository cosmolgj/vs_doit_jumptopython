
# slicing with list

a = [1, 2, 3, 4, 5]
print(a[0:2])

# calculate with list

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

print(a*3)

print("length of a list: {0}".format(len(a)))

# correct and delete

a[2] = 4
print("correct result : {0}".format(a[2]))

print("a list : {0}".format(a))

del a[1]

print("delete a[1]: {0}".format(a))

a = [1, 2, 3, 4, 5]

print("a list: {0}".format(a))

del a[2:]
print("result of del a[2:] : {0}".format(a))

# append to list

a = [1, 2, 3, 4]
print("list a : {0}".format(a))
a.append(5)
print("result of append(5): {0}".format(a))

# sort of list

a = [5, 2, 4, 3, 1]
print("\nunsorted list: {0}".format(a))
a.sort()
print("sorted list: {0}".format(a))


# reverse of list
a = ['a', 'b', 'c', 'd']
print("\nbase list: {0}".format(a))
a.reverse()
print("reversed list: {0}".format(a))

# insertion of list

a = [1, 2, 3]
print("\nlist a : {0}".format(a))
a.insert(0, 4)
print("insert(0, 4) : {0}".format(a))


# remove one of list

a = [1, 2, 3, 1, 2, 3]
print("\nlist a: {0}".format(a))
a.remove(3)
print("remove 3 of list a: {0}".format(a))

# pop of list
a = [1, 2, 3]
print("\nlist a: {0}".format(a))
print("popped value: {0}".format(a.pop()))
print("result of a list: {0}".format(a))

# extention of list
a = [1, 2, 3]
print("\nbefore extention of list a: {0}".format(a))
a.extend([4, 5])
print("after extention [4, 5] of list [1, 2, 3]: {0}".format(a))
