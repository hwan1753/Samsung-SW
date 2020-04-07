T = int(input())
for test_case in range(1,1+T):
    N, M = map(int,input().split())
    tri = []
    count = 0
    for a in range(N):
        tri.append([0 * a for a in range(N)])
    for a in range(M):
        x, y = map(int,input().split())
        tri[x-1][y-1] = tri[y-1][x-1] = 1
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if tri[i][j] and tri[i][k] and tri[j][k]:
                    count += 1
    print("#{} {}".format(test_case,count))