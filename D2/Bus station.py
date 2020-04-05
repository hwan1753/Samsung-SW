T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    array_station = []
    array_count = []
    route = []
    for aa in range(N):
        route.append(list(map(int,input().split())))
    P = int(input())
    for bb in range(P):
        array_station.append(int(input()))
        array_count.append(0)

    for a in route:
        A, B = a[0], a[1]
        for aa in range(array_station.index(A),array_station.index(B)+1):
            array_count[aa] += 1
    print("#{}".format(test_case),end=' ')
    for a in array_count:
        print(a,end=' ')
    print()