T = int(input())
for test_case in range(1,T+1):
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    money = int(input())
    while(money != 0):

        if money >= 50000:
            a = money // 50000
            money = money % 50000
        elif money >= 10000:
            b = money // 10000
            money = money % 10000
        elif money >= 5000:
            c = money // 5000
            money = money % 5000
        elif money >= 1000:
            d = money // 1000
            money = money % 1000
        elif money >= 500:
            e = money // 500
            money = money % 500
        elif money >= 100:
            f = money // 100
            money = money % 100
        elif money >= 50:
            g = money // 50
            money = money % 50
        else:
            h = money // 10
            money = 0
    print("#" + str(test_case))
    print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e) + " " + str(f) + " " + str(g) + " " + str(h))