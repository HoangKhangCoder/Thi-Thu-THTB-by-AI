"""
BÀI 2: DI CHUYỂN - TÌMĐƯỜNG ĐI CÓ SỐ 0 TẬN CÙNG LỚN NHẤT

Yêu cầu: Tìm đường đi từ (1,1) đến (N,M) sao cho tích các số trên đường
có số chữ số 0 tận cùng là lớn nhất.

Nhận xét quan trọng:
- Số chữ số 0 tận cùng = min(số thừa số 2, số thừa số 5)
- Cần tính số thừa số 2 và 5 của tích trên đường đi
- Sử dụng DP với 2 trạng thái: dp[i][j][2] và dp[i][j][5]

Cách giải:
1. Tích có 0 thì tổng chỉ số 0 tận cùng = -∞
2. Ngược lại, cộng số thừa số 2 và 5 từ mỗi ô
3. Số 0 tận cùng = min(count_2, count_5)

Độ khó: Trung bình (cần hiểu về thừa số nguyên tố)
"""

def count_factor(n, factor):
    # Đếm số thừa số 'factor' trong n
    if n == 0:
        return float('inf')  # 0 có vô hạn thừa số 2 và 5
    count = 0
    while n % factor == 0:
        count += 1
        n //= factor
    return count

def solve():
    N, M = map(int, input().split())
    grid = []
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    # dp[i][j] = (max_count_of_2, max_count_of_5) trên đường đi từ (0,0) đến (i,j)
    INF = float('-inf')
    dp2 = [[INF] * M for _ in range(N)]  # Đếm thừa số 2
    dp5 = [[INF] * M for _ in range(N)]  # Đếm thừa số 5

    # Khởi tạo ô đầu tiên
    if grid[0][0] == 0:
        dp2[0][0] = INF
        dp5[0][0] = INF
    else:
        dp2[0][0] = count_factor(grid[0][0], 2)
        dp5[0][0] = count_factor(grid[0][0], 5)

    # Điền hàng đầu tiên
    for j in range(1, M):
        if grid[0][j] == 0:
            dp2[0][j] = INF
            dp5[0][j] = INF
        elif dp2[0][j-1] != INF:
            dp2[0][j] = dp2[0][j-1] + count_factor(grid[0][j], 2)
            dp5[0][j] = dp5[0][j-1] + count_factor(grid[0][j], 5)

    # Điền cột đầu tiên
    for i in range(1, N):
        if grid[i][0] == 0:
            dp2[i][0] = INF
            dp5[i][0] = INF
        elif dp2[i-1][0] != INF:
            dp2[i][0] = dp2[i-1][0] + count_factor(grid[i][0], 2)
            dp5[i][0] = dp5[i-1][0] + count_factor(grid[i][0], 5)

    # Điền phần còn lại
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] == 0:
                dp2[i][j] = INF
                dp5[i][j] = INF
            else:
                factor2 = count_factor(grid[i][j], 2)
                factor5 = count_factor(grid[i][j], 5)

                # Lấy đường đi tốt nhất từ trên hoặc trái
                if dp2[i-1][j] != INF and dp5[i-1][j] != INF:
                    dp2[i][j] = dp2[i-1][j] + factor2
                    dp5[i][j] = dp5[i-1][j] + factor5

                if dp2[i][j-1] != INF and dp5[i][j-1] != INF:
                    dp2[i][j] = max(dp2[i][j], dp2[i][j-1] + factor2)
                    dp5[i][j] = max(dp5[i][j], dp5[i][j-1] + factor5)

    # Kết quả: số 0 tận cùng = min(count_2, count_5)
    result = min(dp2[N-1][M-1], dp5[N-1][M-1])
    print(int(result) if result != INF else -1)

solve()
