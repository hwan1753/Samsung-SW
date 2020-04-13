T = int(input())
for test_case in range(1,1+T):
    N, Q = map(int,input().split())
    array = [0 for _ in range(N)]
    for a in range(1,Q+1):
        L, R = map(int,input().split())
        for b in range(L-1,R):
            array[b] = a
    print("#%d" % test_case,end=' ')
    for c in array:
        print(c,end= ' ')
    print()