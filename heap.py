def maxh(a, i):
    i1 = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(a) and a[i] < a[left]:
        i = left
    if right < len(a) and a[i] < a[right]:
        i = right
    if i1 != i:
        a[i], a[i1] = a[i1], a[i]
        maxh(a, i)


def minh(a, i):
    i1 = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(a) and a[i] > a[left]:
        i = left
    if right < len(a) and a[i] > a[right]:
        i = right
    if i1 != i:
        a[i], a[i1] = a[i1], a[i]
        minh(a, i)
    






def maxhsort(a):
    for i in range(len(a) - 1, 0, -1):
        maxh(a, i)
    for i in range(len(a) - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        maxh(a, i)
    print(a)

def minhsort(a):
    for i in range(len(a) - 1, 0, -1):
        minh(a, i)
    for i in range(len(a) - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        minh(a, i)
    print(a)


a = [4, 10, 3, 5, 1]
maxhsort(a)
minhsort(a)