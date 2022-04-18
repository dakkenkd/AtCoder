"ダブリングライブラリ"

def doubling_idx(lst, k):

    dbl = [[-1]*n for _ in range(56)]

    for i in range(n):
        dbl[0][i] = "ここに初期化する処理を書く"

    for i in range(55):
        for j in range(n):
            dbl[i+1][j] = dbl[i][dbl[i][j]]

    now = "初期値を設定"

    for i in range(56):
        if k >> i & 1:
            now = dbl[i][now]

    return now


def doubling_sum(lst, n, k):

    nxt_dbl = [[-1]*n for _ in range(56)]
    sum_dbl = [[-1]*n for _ in range(56)]

    for i in range(n):
        nxt_dbl[0][i] = "ここに初期化する処理を書く"
        sum_dbl[0][i] = lst[i]

    for i in range(55):
        for j in range(n):
            nxt_dbl[i+1][j] = nxt_dbl[i][nxt_dbl[i][j]]
            sum_dbl[i+1][j] = sum_dbl[i][j] + sum_dbl[i][nxt_dbl[i][j]]

    ans = 0
    curr = "初期値を設定"

    for i in range(56):
        if k >> i & 1:
            ans += sum_dbl[i][curr]
            curr = nxt_dbl[i][curr]

    return ans
