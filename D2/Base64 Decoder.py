T = int(input())
for test_case in range(1,T+1):
    # a = 'Z' #65
    # b = 'a' #97
    # c = '0' #48
    # d = '+' #43
    # e = '/' #47
    i = input()
    array = []
    add = ''
    for x in range(len(i)):

        if ord(i[x]) >= 65 and ord(i[x]) <91:
            a = bin(ord(i[x]) - 65)[2:]
        elif ord(i[x]) >= 91:
            a = bin(ord(i[x]) - 71)[2:]
        elif ord(i[x]) >= 48:
            a = bin(ord(i[x]) + 4)[2:]
        elif ord(i[x]) == 43:
            a = bin(ord(i[x]) + 19)[2:]
        else:
            a = bin(ord(i[x]) + 16)[2:]

        if len(a) < 6:
            for idx in range(6-len(a)):
                a = "0" + a
        add += a
    print("#" + str(test_case) + " ", end='')
    for idx in range(8,len(add),8):
        print(chr(int("0b" + add[idx-8:idx],2)),end='')
    print(".")