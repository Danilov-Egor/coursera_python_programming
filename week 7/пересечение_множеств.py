n = set(list(map(int, input().split())))
f = set(list(map(int, input().split())))
print(*sorted(n & f))
