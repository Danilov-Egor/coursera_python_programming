S, N = list(map(int, input().split()))
users = []
for _ in range(N):
    users.append(int(input()))

users_sorted = sorted(users)
summ = 0

for i in range(1, len(users_sorted) + 1):
    users_cut = users_sorted[:i]
    summ = sum(users_cut)
    if summ <= S:
        number = i
print(number)
