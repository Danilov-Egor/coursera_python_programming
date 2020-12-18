file = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
lines = file.readlines()
z = []
for line in lines:
    line_strip = line.strip().split()
    z.append((line_strip[0] + " " + line_strip[1], line_strip[3]))
z.sort()
for tuple_z in z:
    print(tuple_z[0] + " " + tuple_z[1], file=fout)
