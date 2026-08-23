"""
BÀI 7: CHẤN ĐỘNG WORLD CUP - ĐẾM PARTITION

Yêu cầu: Tính số cách phân hoạch N tệp tài liệu thành các nhóm không trống
(không tính thứ tự các nhóm)

Đây chính là Partition Number p(N)

Ví dụ:
- N=3: [3], [2,1], [1,1,1] -> 3 cách
- N=5: [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1] -> 7 cách

Cách giải:
- Sử dụng DP: dp[n] = số cách phân hoạch n
- dp[n] = sum(dp[n-i] cho mỗi i từ 1 đến n)
- Nhưng cần tối ưu: sử dụng hàm sinh

Công thức DP tối ưu:
- dp[n][k] = số cách phân hoạch n thành các phần có kích thước <= k
- dp[n][k] = dp[n][k-1] + dp[n-k][k]

Độ khó: Khó (cần hiểu DP partition)
"""

MOD = 10**9 + 7

def solve():
    N = int(input())

    # DP: dp[n][k] = số cách phân hoạch n sử dụng các số từ 1 đến k
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Base case: dp[0][k] = 1 (một cách: không có gì)
    for k in range(N + 1):
        dp[0][k] = 1

    # Điền bảng DP
    for n in range(1, N + 1):
        for k in range(1, N + 1):
            # Không sử dụng số k
            dp[n][k] = dp[n][k - 1]

            # Sử dụng số k (ít nhất 1 lần)
            if n >= k:
                dp[n][k] = (dp[n][k] + dp[n - k][k]) % MOD

    print(dp[N][N])

solve()
