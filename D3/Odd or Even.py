T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    if N % 2 == 1:
        print("#{} Odd".format(test_case))
    else:
        print("#{} Even".format(test_case))