a = [1,3,5,7,8,10,12]
b = [2,4,6,9,11]
T = int(input())
for test_case in range(1,1+T):
    m, d = map(int,input().split())
    if m < 3:
        day = ((m - 1) * 31 + d + 3) % 7
    else:
        if m in a:
            if m > 7:
                day = ((m // 2) * 31 + ((m-1) // 2) * 30 - 1 + 3 + d) % 7
            else:
                day = ((m // 2) * 31 + (m // 2) * 30 - 1 + 3 + d) % 7
        else:
            if m > 7:
                day = (((m + 1) // 2) * 31 + ((m - 2) // 2) * 30 - 1 + 3 + d) % 7
            else:
                day = ((m // 2) * 31 + ((m - 2) // 2) * 30 - 1 + 3 + d) % 7
    print("#{} {}".format(test_case, day))