T = int(input())
for test_case in range(1,1+T):
    A, B, C = map(int,input().split())
    if B > A:
        result = C // A
    else:
        result = C // B
    print("#{} {}".format(test_case,result))