T = int(input())
for test_case in range(1,1+T):
    S = list(map(str,input()))
    count = int(input())
    chk = [0 for _ in range(len(S)+1)]
    # chk = 0
    i = list(map(int,input().split()))
    for a in i:
        chk[a] += 1
    print("#{} ".format(test_case), end='')
    for a in range(0,len(S)):
        if chk[a] == 0:
            print(S[a],end='')
        else:
            print('-' * chk[a], end='')
            print(S[a], end='')
    print('-' * chk[len(S)])

