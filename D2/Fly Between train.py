T = int(input())
for test_case in range(1,1+T):
    D, A, B, F = map(int,input().split())
    t = D / (A + B) * F
    print("#{} {}".format(test_case,t))