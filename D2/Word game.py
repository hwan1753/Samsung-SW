T = int(input())
for test_case in range(1,T+1):
    i = list(map(int,input().split()))
    N, K = i[0], i[1]
    block_a, block_b = [], []
    result,chk, total = 0, 0, 0
    for a in range(N):
        block_a.append(list(map(int,input().split())))
        block_b.append([])
    for b in range(N):
        for c in range(N):
            block_b[b].insert(c, block_a[c][b])
    for row in range(N):
        for a in range(N):
            if block_a[row][a] == 1:
                chk += 1
            else:
                if chk == K:
                    total += 1
                chk = 0
        if chk == K:
            total += 1
        chk = 0

    for column in range(N):
        for a in range(N):
            if block_b[column][a] == 1:
                chk += 1
            else:
                if chk == K:
                    total += 1
                chk = 0
        if chk == K:
            total += 1
        chk = 0
    print("#" + str(test_case) + " " +str(total))