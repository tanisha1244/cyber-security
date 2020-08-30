import sys

n = int(sys.argv[1])

f = 0
g = 1

for i in range(0, n):
    f = f + g
    g = f - g
    print(f)

