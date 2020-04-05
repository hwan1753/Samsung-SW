T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    i = input().split()
    array = []
    for a in range(N):
        array.append(0)
    count = 0
    for num in range(len(i)):
        chk = 0
        only = True
        for st in i[num]:
            if st.isupper() == True:
                chk += 1
            if st.isnumeric() == True:
                only = False
                break
        if chk == 1 and only == True:
            array[count] += 1
        if '.' in i[num] or '!' in i[num] or '?' in i[num]:
            count += 1
    print("#{}".format(test_case),end=' ')
    for a in array:
        print(a,end=' ')
    print()