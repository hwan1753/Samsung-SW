T = int(input())
for test_case in range(1,T+1):
    chk_a, chk_b = 0, 1
    plus, mul = 0, 1
    for a in range(1,10):
        chk_a += a
        chk_b *= a
    stop = False
    for a in range(9):
        i = list(map(int,input().split()))
        for num in i:
            mul *= num
        if sum(i) != chk_a or mul != chk_b:
            stop = True
    if stop == True:
        print("#" + str(test_case) + " 0")
    else:
        for sq1 in range(2,3,9):
            for sq2 in range(2,3,9):
                for a in range(sq1):
