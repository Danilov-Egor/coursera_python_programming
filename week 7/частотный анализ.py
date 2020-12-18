fIn = open('input.txt')
myDict = {}
for word in fIn.read().split():
    myDict[word] = myDict.get(word, 0) + 1
myList = sorted(myDict.items())
myList.sort(key=lambda x: x[1], reverse=True)
for word in myList:
    print(word[0], sep='\n')
