T = int(input())
for test_case in range(1,T+1):
    i = list(map(int,input().split()))
    N, K = i[0], i[1] - 1
    sdt,rank = [],[]
    for idx in range(N):
        a = list(map(int,input().split()))
        sdt.append(a[0]*0.35 + a[1]*0.45 + a[2]*0.2)
    sdt_rank = sorted(sdt)
    for cnt in range(len(sdt_rank)):
        if sdt[K] == sdt_rank[cnt]:
            if cnt // (N // 10) == 0:
                print("#" + str(test_case) + " D0")
            elif cnt // (N // 10) == 1:
                print("#" + str(test_case) + " C-")
            elif cnt // (N // 10) == 2:
                print("#" + str(test_case) + " C0")
            elif cnt // (N // 10) == 3:
                print("#" + str(test_case) + " C+")
            elif cnt // (N // 10) == 4:
                print("#" + str(test_case) + " B-")
            elif cnt // (N // 10) == 5:
                print("#" + str(test_case) + " B0")
            elif cnt // (N // 10) == 6:
                print("#" + str(test_case) + " B+")
            elif cnt // (N // 10) == 7:
                print("#" + str(test_case) + " A-")
            elif cnt // (N // 10) == 8:
                print("#" + str(test_case) + " A0")
            else:
                print("#" + str(test_case) + " A+")