T = int(input())
for test_case in range(1,T+1):
    i = list(map(int,input().split()))
    date = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_a, day_a = i[0], i[1]
    month_b, day_b = i[2], i[3]
    total_a, total_b = 0, 0
    for a in range(month_a-1):
        total_a += date[a]
    total_a += day_a
    for b in range(month_b-1):
        total_b += date[b]
    total_b += day_b

    print("#" + str(test_case) + " " + str(total_b - total_a + 1))