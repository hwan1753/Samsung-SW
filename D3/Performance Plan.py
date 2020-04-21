T = int(input())
for test_case in range(1,1+T):
    i = list(map(int,(map(str,input()))))
    total = i[0]
    count = 0
    for a in range(1,len(i)):
        if total >= a:
            total += i[a]
        else:
            count += a - total
            total = a + i[a]
    print("#%d %d" %(test_case, count))