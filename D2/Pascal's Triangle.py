T= int(input())
for test_case in range(1,T+1):
    N = int(input())
    print("#" + str(test_case))
    array_a = [1]
    array_print = []
    print(array_a[0])
    for row in range(2,N+1):
        if row != 2:
            array_a = []
            for a in range(row):
                if a == 0 or a == row-1:
                    array_a.append(1)
                else:
                    array_a.append(array_print[a-1] + array_print[a])
        else:
            array_a.append(1)
        array_print = array_a[:]
        for num in array_print:
            print(num, end= ' ')
        print()