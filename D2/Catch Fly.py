T = int(input())
for test_case in range(1,T+1):
    A = list(map(int,input().split()))
    N, M, c = A[0], A[1], A[1]
    array_n = []
    array_m = []
    array_t = []
    total ,result = 0, 0
    for n in range(1,N+1):
        array_n.append(list(map(int,input().split())))
    for idx in range(N):
        array_m.append([])
        for a in range(N-M+1):
            array_m[idx].append(sum(array_n[idx][a:a+M]))

    for a in range(N-M+1):
        for idx in range(N-M+1):
            for b in range(M):
                total += array_m[idx+b][a]
            if total > result: result = total
            total = 0

    print("#" + str(test_case) + " " + str(result))