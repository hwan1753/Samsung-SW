T = int(input())
for test_case in range(1,1+T):
    a, b = input().split(' ')
    result_b = ''
    idx_a = 0
    for idx_b in range(len(b)):
        stop = False
        while (stop==False):
            if b[idx_b] == a[idx_a]:
                chk = idx_a
                result_b += b[idx_b]
                break
            else:
                if idx_a != len(a)-1:
                    idx_a += 1
                else:
                    stop = True
                    idx_a = chk
    idx_b = 0
    result_a = ''
    for idx_a in range(len(a)):
        stop = False
        while (stop==False):
            if a[idx_a] == b[idx_b]:
                chk = idx_b
                result_a += a[idx_a]
                break
            else:
                if idx_b != len(a)-1:
                    idx_b += 1
                else:
                    stop = True
                    idx_b = chk
    if len(result_a) > len(result_b):
        print("#{} {}".format(test_case,len(result_a)))
    else:
        print("#{} {}".format(test_case, len(result_b)))