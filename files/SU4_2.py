
N = int(input("Give a number: "))
S = 0

for i in range(1, N+1):
    if ((i % 2) == 0):
        S= S + i
        print(S)