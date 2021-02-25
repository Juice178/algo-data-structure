# 3.3
# N(2)個の相異なる整数a0,a1,...,aN－1が与えられます．
# このうち２番目に小さい値を求めるO(N)のアルゴリズムを設計してください



def main() -> None:
    n = int(input("n = "))
    a = []
    for i in range(n):
        a.append(int(input(f"a[{i}] = ")))

    smallest_num, second_smallest_num = float('inf'), float('inf')
    for i in range(len(a)):
        if a[i] < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = a[i]
        elif smallest_num < a[i] and a[i] < second_smallest_num:
            second_smallest_num = a[i]

    print(second_smallest_num)


if __name__ == "__main__":
    main()