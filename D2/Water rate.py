T = int(input())
for test_case in range(1,T+1):
    i = list(map(int,input().split()))
    P, Q, R, S, W = i[0], i[1], i[2], i[3], i[4]

    a = P * W
    if W <= R:
        b = Q
    else:
        b = Q + (W - R) * S
    if a > b:
        print("#" + str(test_case)+ " " + str(b))
    else:
        print("#" + str(test_case)+ " " + str(a))
