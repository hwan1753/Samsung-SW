T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    if N % 2 == 1:
        print("#" + str(test_case) + " " + str(N // 2 + 1))
    else:
        print("#" + str(test_case) + " " + str(-1 * (N // 2)))