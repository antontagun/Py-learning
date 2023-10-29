# Марсианин

dct = {}
dct_day = {}
num = int(input())
b = 0
c = 10000000000000000000000000000000
for i in range(num):
    a = input().split()
    dct[a[0]] = int(a[1])
for i in range(num):
    d = input().split()
    dct_day[d[0]] = int(d[1])
for i in dct:
    b = dct[i] // dct_day[i]
    if b < c:
        c = b
print(c)

#Дистанционный курс

dct = {}
num = int(input())
for i in range(num):
    a = input().split(': ')
    if a[0] not in dct:
        dct[a[0]] = int(a[1])
    else:
        dct[a[0]] += int(a[1])

for i in dct:
    if dct[i] >= 75:
        print(i)

#Физические термины

a = input()
dct = {}
while a != '':
    a = a.split(': ')
    dct[a[1]] = a[0]
    a = input()

num = int(input())
for i in range(num):
    b = input()
    if b in dct:
        print(dct[b])