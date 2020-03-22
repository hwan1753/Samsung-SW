T = int(input())
for test_case in range(1,T+1):
    i = list(map(int,input().split()))
    hour = [i[0],i[2]]
    minute = [i[1],i[3]]
    if sum(minute) >= 60:
        result_m = sum(minute) % 60
        result_h = sum(hour) % 12 + 1
    else:
        result_m = sum(minute)
        result_h = sum(hour) % 12
    print("#" + str(test_case) + " " +str(result_h) + " " + str(result_m))
