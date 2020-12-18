N = int(input())
a = list(map(int, input().split()[:N]))
b = sorted(a, reverse=False)
print(*b)
