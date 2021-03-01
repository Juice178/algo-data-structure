def fibo(N: int) -> int:
    F = [0] *  N
    F[0], F[1] = 0, 1
    for i in range(2, len(F)):
        F[i] = F[i-1] + F[i-2]
        print(f"{i}: {F[i]}")


if __name__ == "__main__":
    fibo(50)