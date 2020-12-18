N = int(input())
s = []
for _ in range(N):
    n = list(input().split())
    s.append((int(n[1]), n[0]))
s.sort(reverse=True)
for elem in s:
    print(elem[1])
