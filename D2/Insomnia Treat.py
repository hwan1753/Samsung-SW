T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    stop = False
    array = [0,1,2,3,4,5,6,7,8,9]
    chk = []
    count = 1
    num = N
    while (stop != True):
        string = str(num)
        for a in string:
            if int(a) not in chk:
                chk.append(int(a))
        chk = sorted(chk)
        if array == chk:
            print("#" + str(test_case) + " " + str(num))
            stop = True
        else:
            count += 1
            num = count * N
