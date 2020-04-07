T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    i = list(map(int,input().split()))
    result = -1
    # for a in range(len(i)-1,-1,-1):
    #     for b in range(a,-1,-1):
    #         mul = str(i[a] * i[b])
    #         chk = len(mul)
    #         for c in chk:

    for a in range(N-1):
        for b in range(a+1,N):
            mul = str(i[a] * i[b])
            stop = False
            # if int(mul) < result:
            #     stop = True
            idx = 0
            while (stop == False):
                if len(mul)-1>idx:
                    if mul[idx] <= mul[idx+1]:
                        idx += 1
                    else:
                        stop = True
                else:
                    if int(mul) > result:
                        result = int(mul)
                    stop = True
    print("#{} {}".format(test_case,result))