#완전탐색
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split(' ')))
    total_b = 0
    stop = False
    while (stop == False):
        a = num.index(max(num))
        if a == 0:
            del num[0]
            if len(num) == 0:
                stop = True
        else:
            total_b += num[a] * a - sum(num[:a])
            if a + 1 != len(num):
                del num[:a+1]
            else:
                stop = True
    print("#" + str(test_case) + " " + str(total_b))
