'''
# Q2
num = 0
sum = 0

while num < 1000:
    if num % 3 == 0:
        sum = sum + num
    
    num = num + 1

print(sum)
    
'''

'''
# Q3
num = 1
while num < 6:

    print("*"*num)

    num = num + 1
    
'''

'''
#Q4

for num in range(0, 100):
    print(num+1)
'''

'''
#Q5
sum = 0
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for i in a:
    sum = sum + i

avg = int(sum / len(a))

print(avg)
'''

'''
#Q6

numbers = [1, 2, 3, 4, 5]
result = []

result = [2*n for n in numbers if n%2 == 1]

print(result)
'''



f = open("C:/new.txt", 'w')
for i in range(1, 11):
    data = "%dth line.\n" % i
    f.write(data)
f.close()