n = int(input())
g = []
for i in range(0, n):
    synonims = list(input().split())
    synonims = tuple(synonims)
    g.append(synonims)
dictionary = dict(g)
word = input()
for word1, word2 in dictionary.items():
    if word1 == word:
        print(word2)
    if word2 == word:
        print(word1)
