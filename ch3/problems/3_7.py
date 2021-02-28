# 3.7
# 各桁の値が１以上９以下の数値のみである整数とみなせるような，長さNの文字列Sが与えられます．この文字列の中で，文字と文字の間
# のうちのいくつかの場所に「＋」を入れることができます．１つも入れなくてもかまいませんが，「＋」が連続してはいけません．
# このようにしてできるすべての文字列を数値とみなして，総和を計算するO(N2^N)のアルゴリズムを設計してください


def main() -> None:
    s = input("s = ").strip()
    n = len(s)

    sum_val = 0

    for bit in range(1 << (n-1)):
        # 両端が+で挟まれた数字(+tmp+)
        tmp = 0
        for i in range(n-1):
            tmp *= 10
            tmp += int(s[i])

            if (bit & (1 << i)):
                # +を挿入された桁までの合計値を計算する
                sum_val += tmp
                # 初期化
                tmp = 0
        # 最後の数字を合計値に足す
        tmp *= 10
        tmp += int(s[-1])
        sum_val += tmp

    print(sum_val)

if __name__ == "__main__":
    main()