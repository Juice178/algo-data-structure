import sys
from typing import List


INF: int = 20000000

def main(argv) -> None:
    N: int = int(argv[0])
    a: List[int] = []
    print(f"Please enter an integer value for a list with the size of {N} ")
    for i in range(N):
        a.append(int(input(f"Index at {i} ")))
    
    min_value: int = INF

    for i in range(N):
        if a[i] < min_value:
            min_value = a[i]
        # min_value = a[i] if a[i] < min_value else min_value
    
    print(f"Mimimum value is: {min_value}")


if __name__ == '__main__':
    main(sys.argv[1:])