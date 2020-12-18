n = list(map(int, input().split()))
f = set()
for i in n:
    if i in f:
        print('YES')
    else:
        print('NO')
        f.add(i)
