import sys
from typing import List


INF: int = 20000000

def main(argv) -> None:
    N: int = int(argv[0])
    W: int = int(argv[1])
    a: List[int] = []
    
    print(f"Please enter an integer value for a list with the size of {N} ")
    for i in range(N):
        a.append(int(input(f"a[{i}] = ")))
    
    exist: bool = False
    bit: int = 0
    for bit in range(0, 1 << N):
        sum_value: int = 0
        for i in range(N):
            if (bit & (1 << i)):
                sum_value += a[i]

        if sum_value == W:
            exist = True

    print("Yes") if exist else print("No")



if __name__ == '__main__':
    main(sys.argv[1:])
