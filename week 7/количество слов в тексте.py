inFile = open('input.txt', 'r', encoding='utf-8')
n = list(map(str, inFile.read().split()))
s = set(n)
print(len(s))
