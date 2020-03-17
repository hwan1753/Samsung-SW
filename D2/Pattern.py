N = int(input())
for test_case in range(1,N+1):
    string = list(map(str,input()))
    result = 0
    stop = False
    for a in range(1,11):
        if stop == True:
            break
        for b in range(1, 30 // a + 1):
            if string[(b-1) * a:b * a] != string[b * a : (b + 1) * a]:
                break
            else:
                result = a
                # if 30 % a == 0:
                stop = True
    print("#" + str(test_case) + " " + str(result))