# https://pl.spoj.com/problems/PYREGR/

import numpy as np

m, n, q = map(int, input().split())

OVector = np.zeros(n)
inp = list(map(float, input().split()))

points = np.reshape(inp, (m, n))
yArr = list(map(float, input().split()))

for i in range(0, 1000):
    sum = np.zeros(n)
    for x, y in zip(points, yArr):
        sum += (np.dot(OVector, x) - y)*(x)
    OVector = OVector - 0.01 * (sum / m)

inp = list(map(float, input().split()))
queries = np.reshape(inp, (q, n))
for x in queries:
    print(round(np.dot(OVector, x), 2))
    

"""

4 2 4
1 1 2 1 3 1 4 1
2 3 4 5
5 1 6 1 7 1 8 1

6.092639088312459
7.137612181823215
8.18258527533397
9.227558368844726

6.09
7.14
8.18
9.23



4 2 0
1 1 2 1 3 1 4 1
2 3 4 5


"""