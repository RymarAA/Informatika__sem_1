def qsort(a):
    if len(a) < 2:
        return a
    m = a[len(a)//2]
    return qsort([el for el in a if el < m]) + [el for el in a if el == m] + qsort([el for el in a if el > m])


a = list(map(int, input().split()))
print(qsort(a))
