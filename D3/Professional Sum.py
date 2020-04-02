T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    i = list(map(int,input().split()))
    result = -999
    a = 0
    chk = 0
    while (a < len(i)):
        while (a < len(i)):
            chk += i[a]
            if chk > result:
                result = chk
            if chk < 0:
                chk = 0
            a += 1
    print("#{} {}".format(test_case,result))