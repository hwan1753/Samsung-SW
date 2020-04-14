T = int(input())
for test_case in range(1,1+T):
    array = []
    chk = None
    for i in range(5):
        x = input()
        array.append([len(x),x])
    print("#%d " % test_case,end= '')
    for a in range(max(array)[0]):
        for b in range(5):
            if a > array[b][0] -1:
                pass
            else:
                print(array[b][1][a],end='')
    print()