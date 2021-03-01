def func(i: int, w: int, a) -> bool:
    # Base Case
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    # Not Choose a[i-1]
    if func(i-1, w, a):
        return True 
    
    # Choose a[i-1]
    if func(i-1, w-a[i-1], a):
        return True 

    return False


def main() -> None:
    n = int(input("N = "))
    w = int(input("W = "))
    a = [0] * n
    for i in range(n):
        a[i] = int(input(f"a[{i}] = "))

    if func(n, w, a):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()