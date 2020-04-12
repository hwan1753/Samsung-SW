T = int(input())
for test_case in range(1,1+T):
    i = list(map(str, input().split(' ')))
    A = list(map(str, i[0]))
    B = list(map(str, i[1]))
    A.insert(0,'-')
    B.insert(0,'-')
    array_result = []
    for x in range(len(B)):
        array_result.append([])
    for b in range(len(B)):
        for a in range(len(A)):
            if A[a] == '-' or B[b] == '-':
                array_result[b].append(0)
            elif A[a] == B[b]:
                array_result[b].append(array_result[b-1][a-1]+1)
            else:
                if array_result[b][a-1] > array_result[b-1][a]:
                    array_result[b].append(array_result[b][a-1])
                else:
                    array_result[b].append(array_result[b-1][a])
    print("#{} {}".format(test_case,array_result[len(B)-1][len(A)-1]))
