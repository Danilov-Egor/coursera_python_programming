N = str(input())
z = 0
if len(N) == 1:
    N = "000" + N
elif len(N) == 2:
    N = "00" + N
elif len(N) == 3:
    N = "0" + N
if N[0] == N[3]:
    if N[1] == N[2]:
        z = 1
print(z)
