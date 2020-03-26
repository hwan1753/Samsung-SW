T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    C, K = [], []
    count = 1
    for idx in range(1,1+N):
        i = input().split()
        C.append(i[0])
        K.append(int(i[1]))
    print("#" + str(test_case))
    for a in range(len(C)):
        for x in range(K[a]):
            print(C[a], end='')
            count += 1
            if count % 10 == 1:
                print()
    print()