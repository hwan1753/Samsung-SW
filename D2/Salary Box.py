T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    total = 0
    for num in range(N):
        i = list(map(float,input().split()))
        p = i[0]
        x = int(i[1])
        total += p * x
    print('#%d %.6f' % (test_case, total))