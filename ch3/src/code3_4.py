import sys
from typing import List


INF: int = 20000000

def main(argv) -> None:
    N: int = int(argv[0])
    K: int = int(argv[1])
    a: List[int] = []
    b: List[int] = []
    print(f"Please enter an integer value for a list with the size of {N} ")
    for i in range(N):
        a.append(int(input(f"a[{i}] = ")))

    for i in range(N):
        b.append(int(input(f"b[{i}] = ")))

    min_value: int = INF

    for i in range(N):
        for j in range(N):
            if (a[i] + b[j]) < K:
                continue

            if (a[i] + b[j]) < min_value:
                min_value = a[i] + b[j]
    
    print(f"Mimimum value is: {min_value}")


if __name__ == '__main__':
    main(sys.argv[1:])