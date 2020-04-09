T = int(input())
for test_case in range(1,1+T):
    a, b = input().split(' ')
    result = ''
    idx_a = len(a)-1
    for idx_b in range(len(b)-1,-1,-1):
        stop = False
        while (stop==False):
            if b[idx_b] == a[idx_a]:
                chk = idx_a
                result = b[idx_b] + result
                break
            else:
                if idx_a != 0:
                    idx_a -= 1
                else:
                    stop=True
                    idx_a = chk
    print("#{} {}".format(test_case,len(result)))