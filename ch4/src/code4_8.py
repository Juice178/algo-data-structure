from typing import List


def fibo(N: int, memo: List[int]) -> int:
    #memo = [-1] * N
    if N == 0:
        return 0
    elif N == 1:
        return 1

    print(N, len(memo))
    if memo[N] != -1:
        return memo[N]

    memo[N] = fibo(N-1, memo) + fibo(N-2, memo)
    
    return memo[N]
    
    # return memo[N] = fibo(N-1) + fibo(N-2)


if __name__ == "__main__":
    N = 49
    memo = [-1] * (N+1)
    print(fibo(N, memo))

    for N in range(2, 50):
        print(f"{N}: {memo[N]}")
