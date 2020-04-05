T = int(input())
for test_case in range(1,1+T):
    i = list(map(int,input().split()))
    N, M = i[0], i[1]
    array = []
    chk = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    # a,b,c,d,e,f,g,h =  # [y,x]
    for x in range(N):
        array.append([])
        for y in range(N):
            array[x].append(0)

    array[N//2 - 1][N//2 - 1] = 2
    array[N // 2 - 1][N // 2] = 1
    array[N // 2][N // 2 - 1] = 1
    array[N // 2][N // 2] = 2
    # print(array)

    for num in range(M):
        add = list(map(int,input().split()))
        idx, st = [add[1]-1,add[0]-1], add[2]
        array[idx[0]][idx[1]] = st
        for cc in chk:
            stop = False
            y, x = idx[0]+cc[0], idx[1]+cc[1]
            if y < 0 or y > N - 1 or x < 0 or x > N - 1:
                pass
            elif array[y][x] != 0 and array[y][x] != st:
                while (stop == False):
                    y += cc[0]
                    x += cc[1]
                    if y < 0 or y > N - 1 or x < 0 or x > N - 1:
                        break
                    if array[y][x] == 0:
                        break
                    elif array[y][x] == st:
                        while (stop == False):
                            # print(y,x)
                            y -= cc[0]
                            x -= cc[1]
                            if y == idx[0] and x == idx[1]:
                                stop = True
                            else:
                                array[y][x] = st
                    else:
                        pass
    B, W = 0, 0
    for aa in array:
        for bb in aa:
            if bb == 1:
                B += 1
            elif bb == 2:
                W += 1
    print("#{} {} {}".format(test_case,B, W))