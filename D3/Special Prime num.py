array = ['2','3','5','7']
for num in range(11,10 ** 6,2):
    stop = False
    if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        pass
    else:
        i = round(num ** 0.5) + 1
        for a in range(3, i, 2):
            if num % a == 0:
                stop = True
                break
        if stop == False:
            array.append(str(num))

T = int(input())
for test_case in range(1,1+T):
    D,A,B = map(int,input().split())
    D = str(D)
    chk = 0
    for a in array:
        if int(a) >= B+1:
            break
        if D in a and int(a) >= A:
            print(a)
            chk += 1
    print("#{} {}".format(test_case,chk))
