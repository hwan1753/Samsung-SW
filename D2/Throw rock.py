T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    i = list(map(int,input().split()))
    array = list(map(abs,i))
    a = min(array)
    # print(array)
    # print(a)
    count = 0
    for b in array:
        if a == b:
            count += 1
    print("#" + str(test_case) + " " + str(a) + " " + str(count))