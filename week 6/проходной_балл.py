input_file = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
sum = []
k = int(input_file.readline())
for line in input_file:
    m = line.split()
    if int(m[-1]) > 39 and int(m[-2]) > 39 and int(m[-3]) > 39:
        sum.append(int(m[-1]) + int(m[-2]) + int(m[-3]))
sum.sort(reverse=True)
if len(sum) <= k:
    print(0)
elif sum.count(sum[0]) > k:
    print(1)
elif sum[k:].count(sum[k - 1]) < 1:
    print(sum[:k][-1])
else:
    print(sum[:sum.index(sum[k - 1])][-1])
input_file.close()
