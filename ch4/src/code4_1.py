def func(N: int) -> int:
    if N == 0:
        return 0
    return N + func(N - 1)


if __name__ == "__main__":
    val = func(int(input("Enter a integer ")))
    print(val)