T = int(input())
for test_case in range(1,1+T):
    S = list(map(str,input()))
    # for a in range(len(S)):
    print("..#." * len(S),end='')
    print(".")
    print(".#.#" * len(S),end='')
    print(".")
    for a in range(len(S)):
        print("#.{}.".format(S[a]),end='')
    print("#")
    print(".#.#" * len(S), end='')
    print(".")
    print("..#." * len(S), end='')
    print(".")
