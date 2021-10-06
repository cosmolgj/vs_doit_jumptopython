
# available tuple

a = (1, )
b = 1, 2, 3
c = ()
d = (1, 2, 3)
e = ('a', 'b', ('ab', 'cd'))

# can't delete or change of value of tuple

# slicing
t1 = (1, 2, 'a', 'b')
print("tuple t1: {0}".format(t1))
print("t1[1:]: {0}".format(t1[1:]))


# add tuple

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print("\nt1 of tuple: {0}".format(t1))
print("t2 of tuple: {0}".format(t2))
print("t1 + t2 : {0}".format(t1+t2))

# multiple tuple
t1 = (1, 2)
print("\nt1 : {0}".format(t1))
print("t1 * 3: {0}".format(t1*3))

# length of tuple
t1 = (1, 2, 'a', 'b', a)
print("tuple t1: {0}".format(t1))
print("length of tuple: {0}".format(len(t1)))