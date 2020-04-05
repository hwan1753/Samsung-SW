T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    array_station = []
    array_count = []
    for a in range(5000):
        array_count.append(0)
    route = []
    for aa in range(N):
        route.append(list(map(int,input().split())))
    P = int(input())
    for bb in range(P):
        array_station.append(int(input()))

    for a in route:
        A, B = a[0]-1, a[1]-1
        for aa in range(A,B+1):
            array_count[aa] += 1
    print("#{}".format(test_case),end=' ')
    for a in array_station:
        print(array_count[a-1],end=' ')
    print()