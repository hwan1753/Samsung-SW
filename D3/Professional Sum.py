T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    i = list(map(int,input().split()))
    result = 0
    for num in range(len(i)):
        for a in range(num,len(i)+1):
            chk = sum(i[num:a])
            if result < chk:
                result = chk
    print("#{} {}".format(test_case,result))