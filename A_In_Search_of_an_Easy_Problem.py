input()
problems = list(map(int, input().split()))

if problems.count(1) > 0:
    print("HARD")
else:
    print("EASY")