T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    array = []
    count, num = 1, 1
    for a in range(N):
        array.append([])
        for b in range(N):
            array[a].append(0)
    left, right, up, down = [0,-1], [0,1], [1,0], [-1,0]
    idx = [0,0]
    stop = False
    while (count != (N ** 2)+1):
        if num % 4 == 1:
            if idx[1] + 1 != N and array[idx[0]][idx[1]+1] == 0:
                array[idx[0]][idx[1]] = count
                count += 1
                idx[0] = idx[0] + right[0]
                idx[1] = idx[1] + right[1]
            else:
                array[idx[0]][idx[1]] = count
                count += 1
                num += 1
                idx[0] = idx[0] + up[0]
        elif num % 4 == 2:
            if idx[0] + 1 != N and array[idx[0]+1][idx[1]] == 0:
                array[idx[0]][idx[1]] = count
                count += 1
                idx[0] = idx[0] + up[0]
                idx[1] = idx[1] + up[1]
            else:
                array[idx[0]][idx[1]] = count
                count += 1
                num += 1
                idx[1] = idx[1] + left[1]
        elif num % 4 == 3:
            if idx[1] - 1 != -1 and array[idx[0]][idx[1]-1] == 0:
                array[idx[0]][idx[1]] = count
                count += 1
                idx[0] = idx[0] + left[0]
                idx[1] = idx[1] + left[1]
            else:
                array[idx[0]][idx[1]] = count
                count += 1
                num += 1
                idx[0] = idx[0] + down[0]
        elif num % 4 == 0:
            if idx[0] - 1 != -1 and array[idx[0]-1][idx[1]] == 0:
                array[idx[0]][idx[1]] = count
                count += 1
                idx[0] = idx[0] + down[0]
                idx[1] = idx[1] + down[1]
            else:
                array[idx[0]][idx[1]] = count
                count += 1
                num += 1
                idx[1] = idx[1] + right[1]
    print("#" + str(test_case))
    for idx in array:
        for idx_b in idx:
            print(idx_b, end=' ')
        print()