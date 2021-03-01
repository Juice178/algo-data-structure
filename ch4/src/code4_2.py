def func(N: int) -> int:
    print(f"func(' << {N} << ') is called. ")
    if N == 0:
        return 0
    
    result = N + func(N - 1)
    print(f"Sum until {N} = {result}")

    return result


if __name__ == "__main__":
    val = func(int(input("Enter a integer ")))
    print(val)