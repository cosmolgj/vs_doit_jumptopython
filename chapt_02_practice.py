
'''
# Q1

mr_hong = {'국어':80, '영어':75, '수학':55}

sum = 0

for value in mr_hong.values():
    sum = sum + value

avg = int(sum / len(mr_hong))

print("홍길동의 평균 점수는 {}점 입니다.".format(avg))
'''

# Q2



'''
# Q3

person_id = "881120-1068234"

# print("%d 년 %d 월 %d 일", int(person_id[0:1]), int(person_id[2:3]), int(person_id[4:5]))

print("{} 년 {} 월 {} 일".format(person_id[0:2], person_id[2:4], person_id[4:6]))
print("{}".format(person_id[7:]))

'''
'''
# Q5
a = "a:b:c:d"

print(a.replace(":", "#"))
'''

'''
# Q6
a = [1, 3, 5, 4, 2]

sort_a = a.sort()

for i in a:
    print(i)

'''

'''
# Q7

a = ['Life', 'is', 'too', 'short']

result = " ".join(a)

print(result)

'''

#Q10

a = {'A':90, 'B':80, 'C':70}

print(a.pop('B'))

'''
# Q11

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

set_a = set(a)

print(set_a)
'''