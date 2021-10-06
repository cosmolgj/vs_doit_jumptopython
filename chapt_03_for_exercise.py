
a = [(1,2), (3, 4), (5, 6)]

for (first, last) in a:
    print(first + last)


marks = [90, 25 ,67, 46, 80]

number = 0

for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)


# 9 x 9

for i in range(2, 10):
    for j in range(1, 10):
#        print(i * j, end= " ")
        print("%d x %d = %d" % (i, j, i*j))
    print('')

# list comprehension

a = [1, 2, 3, 4]

result = []

for num in a:
    result.append(num*3)
print(result)

print("{0:=^30}".format(" list comprehension "))
result = [num* 3 for num in a]
print(result)


result = [num*3 for num in a if num % 2 == 0]
print(result)

print("\n{0:=^30}".format(" list comprehension (9x9) "))
result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
