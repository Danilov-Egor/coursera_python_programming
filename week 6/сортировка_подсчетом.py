def CountSort(A):
    c = [0] * 101
    for element in A:
        c[element] += 1
    for elementnow in range(101):
        print((str(elementnow) + ' ') * c[elementnow], end='')


n = list(map(int, input().split()))
CountSort(n)
