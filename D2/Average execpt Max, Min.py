T = int(input())
for test_case in range(1,T+1):
    N = list(map(int,input().split()))
    N.remove(max(N))
    N.remove(min(N))
    print("#" + str(test_case) + " " + str(round(sum(N)/len(N))))