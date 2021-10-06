multiline = """
life is good
but hard
"""

print(multiline)



# formatting

number = 10
day = "five"

state1 = "I ate %d apples. so I was sick for %s days." % (number, day)
print(state1)

print("%10s" % "hi")
print("%10.4f" % 3.241958)

print("I eat {0} apples".format(3))

print("I eat {0} apples.".format("five"))

print("I ate {0} apples. So I was sick for {1} days.".format(6, "five"))

print("I ate {number} apples. So I was sick for {day} days.".format(number=30, day=10))

print("{0:<20}".format("hi"))

print("{0:>20}".format("hi"))

print("{0:^20}".format("hi"))

print("{0:=^20}".format(" hi "))

print("{0:!<20}".format("Hi"))

print("{0:0.4f}".format(3.423421))

print("{0:10.5f}".format(3.42552))

# f formatting
name = 'gildong hong'
age = 'five'
print(f'my name is {name}. I am {age}.')


# f formatting with dictionary
d = {'name':'pooh', 'age':30}
print(f'my name is {d["name"]}. I am {d["age"]}.')

# sorting with f formatting

print(f'{"hi":<20}')

print(f'{"hi":>20}')

print(f'{"hi":^20}')

print(f'{" hi ":=^20}')

print(f'{3.424523:10.4f}')

# counting

print("hobby".count('b'))

# find spell index with string
print("python is the best choice".find('c'))

print("python is the best choice".index('c'))

# join with string

print(", ".join('abcd'))

print(", ".join(['a', 'b', 'c', 'd']))
print(", ".join(('a', 'b', 'c', 'd')))

# upper with string

print("hi".upper())

# lower with string

print("HI".lower())

# lstrip, rstrip, strip

print("   hi   ".lstrip())
print("   hi   ".rstrip())
print("   hi   ".strip())

# replace

print("life is too short".replace("life", "your leg"))

# split

print("life is too short".split())
print("a:b:c:d".split(':'))