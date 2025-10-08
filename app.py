a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 4
res = [a[i:j + n] for i in range(0, len(a), n)]
print(res)
