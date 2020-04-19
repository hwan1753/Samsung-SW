res = []
T = int(input())
for test_case in range(1,1+T):
    A, B, C, D = map(int,input().split()) # 00 01 10 11
    size = A+B+C+D
    # snt = ['-' for _ in range(size+1)]
    top = 0
    stop = False
    if C == 0 and B == 0:
        snt = 'impossible'
    elif B > C:
        top = A + 1
        snt = '0' * A + '1'* D + '1'
        A = 0
        B -= 1
        # for b in range(D+1):
        top += 1
        while stop==False:
            if snt[size] != '-':
                break
            if snt[top-1] == '0' and B != 0:
                B -= 1
                snt[top] = '1'
                top += 1
            elif snt[top-1] == '1' and C != 0:
                C -= 1
                snt[top] = '0'
                top += 1
    else:
        top = D + 1
        for a in range(D + 1):
            snt[a] = '1'
            D = 0
        C -= 1
        for b in range(A+1):
            snt[top] = '0'
            top += 1
        while stop == False:
            if snt[size] != '-':
                break
            if snt[top - 1] == '0' and B != 0:
                B -= 1
                snt[top] = '1'
                top += 1
            elif snt[top - 1] == '1' and C != 0:
                C -= 1
                snt[top] = '0'
                top += 1
    res.append(snt)
# for a in range(len(res)):
#     print("#{} ".format(a+1), end='')
#     for b in res[a]:
#         print(b, end='')
#     print()
