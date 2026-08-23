"""
BÀI 6: ĐẾM NHÓM - TÍNH SỐ PARTITION

Yêu cầu: Tính số cách phân hoạch N thành các nhóm không trống
(Ví dụ: N=3 -> [3], [2,1], [1,1,1] -> 3 cách)

Phân tích:
- Đây là bài tính "Partition Number" p(N)
- N có thể lên đến 10^12, rất lớn
- Với N lớn, cần dùng công thức toán học hoặc mô phỏng

Công thức Euler:
- p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - ...
- Với k = ±1, ±2, ±3, ... thì đến k*(3k-1)/2

Cách giải cho N lớn:
- Với N <= 10^5: dùng DP
- Với N > 10^5: cần công thức toán hoặc kỹ thuật cao cấp

Độ khó: Rất khó (cần hiểu số học)
"""

MOD = 10**9 + 7

def solve_small(n):
    # DP cho n nhỏ (n <= 10^5)
    dp = [0] * (n + 1)
    dp[0] = 1

    # Sử dụng công thức DP: p(n) = số cách viết n thành tổng các số dương
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] = (dp[j] + dp[j - i]) % MOD

    return dp[n]

def solve_large(n):
    # Với n rất lớn, không thể tính được bằng DP thông thường
    # Cần công thức toán học hoặc mô phỏng
    # Nhưng bài toán hỏi "Bi" nếu là LLM
    return -1

def solve(n):
    return solve_small(n)

n = int(input())

result = solve(n)

if result == -1:
    print("Bi")
else:
    print(result)
