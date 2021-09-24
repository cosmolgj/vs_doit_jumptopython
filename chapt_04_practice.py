'''
# Q1

def is_odd(num):
    if (num % 2 == 0):
        print("{} is even.".format(num))
    else:
        print("{} is odd.".format(num))

is_odd(5)
is_odd(10)

# Q1-1

is_odd = lambda x: True if x %2 == 0 else False

'''

'''
# Q2

def cal_average(*args):
    sum = 0
    for i in args:
        sum = sum + i

    avg = int(sum / len(args))

    print("average is {}.".format(avg))

cal_average(20, 50, 80, 40)

'''


'''
# Q5

with open("test.txt", 'w') as f1:
    f1.write("Life is too short")

with open("test.txt", 'r') as f2:
    print(f2.read())
'''

'''
# Q6

print("write to save anything: ")

content = input()

with open("test.txt", '+a') as f:
    f.write(content)
    f.write('\r\n')

with open("test.txt", 'r') as f2:
    print(f2.read())
'''


# Q7

with open("test.txt", 'r') as f:
    lines = f.read()
    new_line = lines.replace('java', 'python')

with open("test.txt", 'w') as f2:
    f2.write(new_line)

