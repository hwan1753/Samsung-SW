result_array = []
T = int(input())
for test_case in range(1,1+T):
    N = int(input())

    if round(N ** (1.0/3.0),10) / int(round(N ** (1.0/3.0),10)) == 1:
        result_array.append(int(round(N ** (1.0/3.0),10)))
    else:
        result_array.append(-1)

for res in range(len(result_array)):
    print("#{} {}".format(res+1, result_array[res]))