n = int(input())
potential_numbers = set([i for i in range(1, n + 1)])
while True:
    beatrise = input()
    if beatrise == 'HELP':
        sorted_set = sorted(potential_numbers)
        print(*sorted_set)
        break
    else:
        beatrise = set(list(map(int, beatrise.split())))
    answer = input()
    if answer == "YES":
        potential_numbers &= beatrise
    else:
        potential_numbers -= beatrise
