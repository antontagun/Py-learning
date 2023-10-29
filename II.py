N, K = [int(x) for x in input().split()]
lst = list(map(int, input().split()))

def entopiya_1(c, lst_1):
    mn2 = 0
    for i in c:
        mn2 += (i/sum(c))**2
    return mn2

def entopiya(z):

    lst_1 = lst[:z]
    lst_2 = lst[z:]

    c = [lst_1.count(i) for i in set(lst_1)], [lst_2.count(i) for i in set(lst_2)]

    t1 = 1 - entopiya_1(c[0], lst_1)
    t2 = 1 - entopiya_1(c[1], lst_2)
    ent = ((sum(c[0]) / N) * t1) + ((sum(c[1]) / N) * t2)
    print(ent)


for i in range(1, N):
    entopiya(i)





