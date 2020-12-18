infile = open('input.txt', 'r', encoding='utf8')
fileOut = open('output.txt', 'w', encoding='utf8')
input_data = infile.readlines()

candidaty = dict()
cand_list = list()
for lk in input_data:
    candidaty[lk] = candidaty.get(lk, 0) + 1
for lk in candidaty:
    cand_list.append((candidaty[lk], lk))
cand_list = sorted(cand_list)
if cand_list[-1][0] > len(input_data) / 2:
    fileOut.writelines(cand_list[-1][1])
else:
    fileOut.writelines(cand_list[-1][1])
    fileOut.writelines(cand_list[-2][1])
