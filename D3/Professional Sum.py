T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    i = list(map(int,input().split()))
    result = []
    for num in range(len(i)):
        stop = False
        idx, chk = 0, -9999
        array_chk = []
        while (stop == False):
            if sum(i[num:num+idx+1]) >= 0 and num + idx + 1 <= len(i):
                chk = sum(i[num:num+idx+1])
                array_chk.append(chk)
                idx += 1
            else:
                if array_chk != []:
                    chk = max(array_chk)
                stop = True
        result.append(chk)
    result.append(max(i))
    print("#{} {}".format(test_case,max(result)))