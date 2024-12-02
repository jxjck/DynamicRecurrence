from argminsum import argminsum, zero, inf, min

def minsumcomb(x: list[int], M: int) -> list[list[argminsum]]:
    N = len(x)
    #convert elements to argminsum type with indices
    x_argminsum = [argminsum(val, [i]) for i, val in enumerate(x)]
    #dp table with argminsum types
    dp = [[zero if m == 0 else inf for m in range(M + 1)] for n in range(N + 1)]
    #compute dp values
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            dp[n][m] = min(dp[n - 1][m], dp[n - 1][m - 1] + x_argminsum[n - 1])
    return dp

if __name__ == "__main__":
    x = [11, 3, -5, 8, 2]
    M = 2
    S = minsumcomb(x, M)

    for i, l in enumerate(S):
        for j, e in enumerate(l):
            print(f"S[{i}][{j}] = {(e.val)}")
    print("---------")
    for i, l in enumerate(S):
        for j, e in enumerate(l):
            print(f"S[{i}][{j}] = {(list(e.cnfg))}")