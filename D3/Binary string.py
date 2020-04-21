res = []
T = int(input())
for test_case in range(1,1+T):
    A, B, C, D = map(int,input().split()) # 00 01 10 11
    if B == 0 and C == 0:
        if D == 0 and A != 0:
            snt = '0' * A + '0'
        elif A == 0 and D != 0:
            snt = '1' * D + '1'
        else:
            snt = 'impossible'
    elif B - C > 1 or C - B > 1:
        snt = 'impossible'
    elif B - C == 1:
        snt = '0' * A + '01' * B + '1' * D
    elif C - B == 1:
        snt = '1' * D + '10' * C + '0' * A
    else:
        snt = '0' * A + '01' * B + '1' * D + '0'
    res.append(snt)
for a in range(len(res)):
    print("#{} ".format(a+1), end='')
    for b in res[a]:
        print(b, end='')
    print()
