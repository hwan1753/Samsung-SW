array = [2,3]
for a in range(4,1000):
    stop = False
    if a % 2 == 0 or a % 3 == 0:
        pass
    else:
        for b in range(4,a):
            if a % b != 0:
                pass
            else:
                stop = True
                break
        if stop != True:
            array.append(a)
result_array = []
T = int(input())
for test_case in range(1,1+T):
    result = 0
    N = int(input())
    for idx in range(len(array)):
        if array[idx] > N:
            chk = idx
            break
    for a in range(idx):
        for b in range(a,idx):
            for c in range(b,idx):
                if array[a] + array[b] + array[c] == N:
                    result += 1
                elif array[a] + array[b] + array[c] > N:
                    break
    result_array.append(result)
for res in range(len(result_array)):
    print("#{} {}".format(res+1,result_array[res]))