T = int(input())
for test_case in range(1,1+T):
    N, K = map(int,input().split())
    chk = [0 for _ in range(N)]
    i = list(map(int,input().split()))
    for a in i:
        chk[a-1] = 1
    print("#%d" % test_case,end=' ')
    for b in range(N):
        if chk[b] == 0:
            print(b+1, end= ' ')
    print()