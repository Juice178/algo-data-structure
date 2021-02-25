# 3.5

# 求めるN個の正の整数a0,a1,...,aN－1が与えられます．
# これらに対して「N個の整数がすべて偶数ならば２で割った値に置き換える」という操作を，
# 操作が行えなくなるまで繰り返します．何回の操作を行うことになるかを求めるアルゴリズムを設計してください

from typing import List


def is_all_even(a) -> bool:
    for i in range(len(a)):
        if a[i] % 2 != 0:
            return False
    return True


def halve_elements(a) -> List[int]:
    for i in range(len(a)):
        a[i] = a[i] / 2
    return a


def main() -> None:
    n = int(input("n = "))
    a = []
    for i in range(n):
        a.append(int(input(f"a[{i}] = ")))

    num_of_operations = 0

    while is_all_even(a):
        a = halve_elements(a)
        num_of_operations += 1

    print(num_of_operations)


if __name__ == "__main__":
    main()