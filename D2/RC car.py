T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    speed, total = 0, 0
    for num in range(1,1+N):
        i = list(map(int,input().split()))
        if len(i) == 2:
            if i[0] == 1:
                speed = speed + i[1]
                total += speed
            else:
                if speed > i[1]:
                    speed = speed - i[1]
                else:
                    speed = 0
                total += speed
        else:
            total += speed
    print("#" + str(test_case) + " " + str(total))
