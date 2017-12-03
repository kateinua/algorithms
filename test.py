l = [10, 1, 10, 10]
h = [5, 50, 5, 5]
n = len(l)
A = [x for x in [0] * (n + 1)]
A[1] = l[0]
for i in range(2, n + 1):
    A[i] = max(A[i - 1] + l[i - 1], A[i - 2] + h[i - 1])
#print(A)

one_week_pause = False
res = []
for i in range(n, 0, -1):
    if one_week_pause:
        one_week_pause = False
        continue
    if A[i] - A[i - 1] == l[i - 1]:
        res.append("low-stress")
    else:
        res.append("high-stress")
        res.append("none")
        one_week_pause = True
res = res[::-1]
result = A[-1]
print(res, result)
