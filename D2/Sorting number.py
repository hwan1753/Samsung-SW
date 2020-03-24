T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    i = sorted(list(map(int,input().split())))
    print("#" + str(test_case) + " ",end='')
    for a in i:
        print(a, end= ' ')
    print()
