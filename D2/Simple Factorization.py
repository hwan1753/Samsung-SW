T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    a,b,c,d,e = 0, 0, 0, 0, 0
    num = N
    while (num != 1):
        if num % 11 == 0:
            e += 1
            num = num // 11
        elif num % 7 == 0:
            d += 1
            num = num // 7
        elif num % 5 == 0:
            c += 1
            num = num // 5
        elif num % 3 == 0:
            b += 1
            num = num // 3
        elif num % 2 == 0:
            a += 1
            num = num // 2
    print("#" + str(test_case) + " " + str(a) + " " + str(b)+ " " + str(c)+ " " + str(d)+ " " + str(e))