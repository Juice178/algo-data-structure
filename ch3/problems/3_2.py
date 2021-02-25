# 3.2
# N個の整数a0,a1,...,aN－1のうち，
# 整数値vが何個含まれるかを求めるO(N)のアルゴリズムを設計してください


def main() -> None:
    n = int(input("n = "))
    v = int(input("v = "))
    a = []
    for i in range(n):
        a.append(int(input(f"a[{i}] = ")))

    count = 0
    for i in range(len(a)):
        if a[i] == v:
            count += 1
    
    print(count)
    


if __name__ == "__main__":
    main()