# from itertools import combinations
# T = int(input())
# for test_case in range(1,1+T):
#     N, L = map(int,input().split())
#     array_T,array_K = [],[]
#     res = 0
#     for i in range(N):
#         T, K = map(int,input().split())
#         array_T.append(T)
#         array_K.append(K)
#     for a in range(1,1+N):
#         array_a = list(combinations(array_K,a))
#         array_b = list(combinations(array_T,a))
#         for b in range(len(array_a)):
#             if sum(array_a[b]) < L and sum(array_b[b]) > res:
#                 res = sum(array_b[b])
#     print("#{} {}".format(test_case,res))

def cal(cnt, score, calo):
    global res
    if cnt == N:
        if calo <= L:
            if score > res:
                res = score
        return

    score_cnt, calo_cnt = arr[cnt]
    cal(cnt + 1, score + score_cnt, calo + calo_cnt)
    cal(cnt + 1, score, calo)


for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    cal(0, 0, 0)

    print(f'#{tc} {res}')