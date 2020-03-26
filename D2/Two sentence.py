T = int(input())
for test_case in range(1,T+1):
    i = list(map(int,input().split()))
    N, M = i[0], i[1]
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    result, cal, count = 0, 0, 0

    if len(A) > len(B):
        dif = len(A) - len(B)
        for x in range(dif):
            B.append(0)
        while (count <= dif):
            for idx in range(len(A)):
                cal += A[idx] * B[idx]
            if cal > result:
                result = cal
            cal = 0
            del B[len(B) - 1]
            B.insert(0, 0)
            count += 1
    else:
        dif = len(B) - len(A)
        for x in range(dif):
            A.append(0)
        while (count <= dif):
            for idx in range(len(A)):
                cal += A[idx] * B[idx]
            if cal > result:
                result = cal
            cal = 0
            del A[len(B) - 1]
            A.insert(0, 0)
            count += 1
    print("#" + str(test_case) + " " + str(result))
