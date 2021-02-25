import sys
from typing import List


def main(argv) -> None:
    N: int = int(argv[0])
    v: int = int(argv[1])
    a: List[int] = []
    for _ in range(N):
        a.append(int(input()))
    
    exist: bool = False
    for i in range(N):
        if a[i] == v:
            exist = True 
    
    print("Yes") if exist else print("No")


if __name__ == '__main__':
    main(sys.argv[1:])