inFile = open('input.txt')
dictWord = {}
for line in inFile:
    for word in line.split():
        dictWord.setdefault(word, 0)
        print(dictWord[word], end='\n')
        dictWord[word] += 1
inFile.close()
