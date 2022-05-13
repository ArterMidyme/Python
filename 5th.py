import itertools
n, k = map(int, input().split())
result = 0
for p in itertools.permutations((i for i in range(1, n + 1)), n):
    sum = 0
    for i in range(n):
        sum += p[i] * (i + 1)
    if sum % k == 0:
        result += 1
print(result)
