total_languages, all_languages = set(), set()
for i in range(int(input())):
    langs = set(input() for _ in range(int(input())))
    total_languages |= langs
    all_languages = all_languages & langs if i else langs
print(len(all_languages), '\n'.join(all_languages), sep='\n')
print(len(total_languages), '\n'.join(total_languages), sep='\n')
