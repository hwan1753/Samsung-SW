T = int(input())
for test_case in range(1,T+1):
    chk_a, chk_b = 0, 1
    for a in range(1,10):
        chk_a += a
        chk_b *= a
    stop = False
    array = []
    sq = []
    vertical = []
    for a in range(1,10):
        mul = 1
        i = list(map(int,input().split()))
        array.append(i)
        for num in i:
            mul *= num
        if sum(i) != chk_a or mul != chk_b:
            stop = True
    # print(array)
    q = 1
    row, column = 0, 0
    for sq1 in range(2,9,3):
        if stop == True:
            break
        for sq2 in range(2,9,3):
            if stop == True:
                break
            mul = 1
            for a in range(row,sq1+1):
                for b in range(column,sq2+1):
                    sq.append(array[b][a])
            q += 1
            for num in sq:
                mul *= num
            if sum(sq) != chk_a or mul != chk_b:
                stop = True
                break
            else:
                sq = []
            column = sq2+1
        row = sq1+1
        column = 0

    for x in range(9):
        mul = 1
        for y in range(9):
            vertical.append(array[y][x])
        for num in vertical:
            mul *= num
        if sum(vertical) != chk_a or mul != chk_b:
            stop = True
            break
        else:
            vertical = []

    if stop == True:
        print("#" + str(test_case) + " 0")
    else:
        print("#" + str(test_case) + " 1")