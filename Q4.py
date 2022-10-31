def dist(values):
    l = []
    for v1, e1, i1 in values:
        for v2, e2, i2 in values:
            if i1 != i2:
                l.append(abs(v1 - v2) + abs(e1 - e2))
    return min(l)

def ex():
    l = []
    n = int(input())
    for i in range(n):
        v, e = [int(j) for j in input().split()]
        l.append((v, e, i))
    print(dist(l))
ex()