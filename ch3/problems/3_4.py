# 3.4
# N個の整数a0,a1,...,aN－1が与えられます．この中から２つ選んで差をとります．
# その差の最大値を求めるO(N)のアルゴリズムを設計してください



def main() -> None:
    n = int(input("n = "))
    a = []
    for i in range(n):
        a.append(int(input(f"a[{i}] = ")))

    smallest_num, largest_num = float('inf'), float('-inf')
    for i in range(len(a)):
        if a[i] < smallest_num:
            smallest_num = a[i]
        if largest_num < a[i]:
            largest_num = a[i]

    print(largest_num - smallest_num)


if __name__ == "__main__":
    main()