T = int(input())
for test_case in range(1,1+T):
    i = list(map(int,input().split()))
    N, M = i[0], i[1]
    array_line = []
    for a in range(M):
        array_line.append(list(map(int, input().split())))
    array_line = sorted(array_line)
    count = 0
    for idx in range(len(array_line)):
        stop = False
        chk = idx
        while (stop == False):
            if chk < len(array_line) -1:
                chk += 1
            else:
                break
            a = array_line[idx]
            b = array_line[chk]
            if a[0] == b[0]:
                if [a[1],b[1]] in array_line:
                    count += 1
            else:
                break
    print("#{} {}".format(test_case,count))