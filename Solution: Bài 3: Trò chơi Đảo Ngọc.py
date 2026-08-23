"""
BÀI 3: TRÒ CHƠI ĐẢO NGỌC - ĐẾM ĐƯỜNG ĐI VÀ TÌM MAX SUM

Yêu cầu:
1. Đếm số đường đi K đảo với tổng giá trị lẻ
2. Tìm tổng giá trị lớn nhất từ K đảo bất kỳ

Ràng buộc: Từ (x,y) chỉ có thể đi tới (x',y') nếu x' >= x và y' >= y

Cách giải:
- Sắp xếp đảo theo tọa độ (x, y)
- DFS/DP để tìm tất cả đường đi độ dài K
- Theo dõi (count_odd_sum, max_sum) cho mỗi trạng thái

Độ khó: Khó (cần DFS + DP kết hợp)
"""

MOD = 10**9 + 7

def solve():
    N, K = map(int, input().split())
    islands = []
    for i in range(N):
        x, y, v = map(int, input().split())
        islands.append((x, y, v, i))

    # Sắp xếp đảo theo tọa độ
    islands.sort()

    # dp[i][j] = (số đường đi j đảo kết thúc tại đảo i với tổng lẻ, max_sum)
    # Nhưng cần lưu cả tất cả đường đi với tổng lẻ/chẵn
    dp = [[{} for _ in range(K + 1)] for _ in range(N)]

    # Khởi tạo: mỗi đảo là đường đi 1 đảo
    for i in range(N):
        x, y, v, idx = islands[i]
        parity = v % 2  # 0 = chẵn, 1 = lẻ
        dp[i][1][parity] = max(dp[i][1].get(parity, 0), v)

    # Tính DP
    for length in range(1, K):
        for i in range(N):
            if not dp[i][length]:
                continue

            x, y, v, idx = islands[i]

            # Cố gắng mở rộng đường đi bằng cách thêm đảo tiếp theo
            for j in range(i + 1, N):
                x2, y2, v2, idx2 = islands[j]

                # Kiểm tra có thể đi từ i đến j không
                if x2 >= x and y2 >= y:
                    for parity, sum_val in dp[i][length].items():
                        new_sum = sum_val + v2
                        new_parity = (parity + v2) % 2

                        if new_parity not in dp[j][length + 1]:
                            dp[j][length + 1][new_parity] = new_sum
                        else:
                            dp[j][length + 1][new_parity] = max(
                                dp[j][length + 1][new_parity], new_sum
                            )

    # Lấy kết quả
    count_odd = 0
    max_sum = -1

    for i in range(N):
        if K in range(len(dp[i])) and dp[i][K]:
            for parity, sum_val in dp[i][K].items():
                if parity == 1:  # Tổng lẻ
                    count_odd = (count_odd + 1) % MOD
                max_sum = max(max_sum, sum_val)

    print(count_odd)
    print(max_sum if max_sum != -1 else -1)

solve()
