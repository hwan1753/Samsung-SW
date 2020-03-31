from itertools import combinations

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    array = []
    test = 'abcdefghijklmnopqrstuvwxyz'
    test_array = []
    count = 0
    for a in test:
        test_array.append(a)
    for num in range(N):
        i = input()
        array.append(i)
    for i in range(N):
        chk = list(map(''.join,combinations(array,i)))
        for idx in chk:
            if len(idx) >= 26:
                for aa in test:
                    if aa in idx:
                        result = 1
                    else:
                        result = 0
                        break
                if result == 1:
                    count += 1
    print("#{} {}".format(test_case,count))