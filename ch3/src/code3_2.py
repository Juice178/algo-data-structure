import sys
from typing import List


def main(argv) -> None:
    N: int = int(argv[0])
    v: int = int(argv[1])
    a: List[int] = []
    for _ in range(N):
        a.append(int(input(f"Please enter an integer value for a list with the size of {N}")))
    
    found_id: int = -1

    for i in range(N):
        if a[i] == v:
            found_id = i
            break
    
    print(f"Index at which v is found is: {found_id}")


if __name__ == '__main__':
    main(sys.argv[1:])