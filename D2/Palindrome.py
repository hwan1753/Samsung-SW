T = int(input())
for test_case in range(1,T+1):
    string_a = list(input())
    string_b = list(reversed(string_a))
    if string_a == string_b: print("#" + str(test_case) + " 1")
    else: print("#" + str(test_case) + " 0")