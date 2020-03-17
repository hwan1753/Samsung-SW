N = int(input())
for a in range(1,N+1):
    if str(a).find('3') != -1 or str(a).find('6') != -1 or str(a).find('9') != -1:
        for b in str(a):
            if b == '3' or b == '6' or b == '9':
                print('-', end='')
        print(' ', end='')
    else:
        print(a, end = ' ')