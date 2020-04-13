result_array = []
T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    a = 1
    while True:
        chk = a * a * a
        if N > chk:
            a += 1
        elif N == chk:
            result_array.append(a)
            break
        else:
            result_array.append(-1)
            break

for res in range(len(result_array)):
    print("#{} {}".format(res+1, result_array[res]))