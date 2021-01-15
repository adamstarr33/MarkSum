import random
def marksum(n):

    a = random.randint(0, 100000000)
    list = []
    if n == 1:
        return 1

    if n == 2:
        list.append(a/100000000)
        list.append((100000000-a)/100000000)
        return list

    list.append(a/100000000)
    temp = a
    for x in range(0,n-2):
        mark = random.randint(0, 100000000-temp)
        list.append(mark/100000000)
        temp = temp + mark
    list.append(1-sum(list))
    return list
# list = []
#
# for x in range(0, n-1):
#     temp = random.randint(0, 1000000)
n = int(input("Oh hi Mark! Please input your desired N value: "))
res = marksum(n)
count = 0
for x in res:
    count+=1
    print(x)
    if count != len(res):
        print("+")
print("=")
print(sum(res))
