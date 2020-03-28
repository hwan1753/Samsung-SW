T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    i = list(map(int,input().split()))
    chk = [0 for a in range(0,101)]
    result = 0
    for a in i:
        chk[a] += 1
    for b in range(len(chk)):
        if chk[b] == max(chk):
            if b > result:
                result = b
    print('#{} {}'.format(test_case,result))