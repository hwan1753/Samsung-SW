T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    array = []
    array_a = []
    array_b = []
    array_c = []
    for num in range(N):
        array.append(list(map(int,input().split())))
    for a in range(N):
        array_a.append([])
        for b in range(N-1,-1,-1):
            array_a[a].append(array[b][a])

    for a in range(N):
        array_b.append([])
        for b in range(N - 1, -1, -1):
            array_b[a].append(array_a[b][a])

    for a in range(N):
        array_c.append([])
        for b in range(N-1,-1,-1):
            array_c[a].append(array_b[b][a])

    print("#" + str(test_case))
    for a in range(N):
        for num in array_a[a]:
            print(num, end='')
        print(' ',end='')
        for num in array_b[a]:
            print(num, end='')
        print(' ',end='')
        for num in array_c[a]:
            print(num, end='')
        print()