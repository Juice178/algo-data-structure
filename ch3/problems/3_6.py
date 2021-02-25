# 3.5

# ２つの正の整数K,Nが与えられます．
# 0 <= X,Y,Z <= Kを満たす整数(X,Y,Z)の組であって
# X＋Y＋Z＝Nを満たすものが何通りあるかを求めるO(N2)のアルゴリズムを設計してください．


def main() -> None:
    k = int(input("k = "))
    n = int(input("n = "))

    num_of_combinations= 0

    for x in range(k+1):
        for y in range(k+1):
            z = n - x- y
            if 0 <= z and z <= k:
                # print(f"x, y, z = {(x, y, z)}")
                num_of_combinations += 1

    print(num_of_combinations)

if __name__ == "__main__":
    main()