"""
BÀI 4: BÍ MẬT CỦA LÃNH CHÚA MÈO BÉO

Yêu cầu: Tìm vị trí đặt máy hút K kho liên tiếp sao cho
Lợi Nhuận = (Tổng hút được) - (Tổng bị chuột cướp) là lớn nhất

Phân tích:
- Đặt máy tại vị trí i: hút từ A[i] đến A[i+K-1]
- Bị cướp: A[i-1] (nếu tồn tại) + A[i+K] (nếu tồn tại)
- Lợi nhuận = sum(A[i:i+K]) - A[i-1] - A[i+K]

Cách giải:
1. Tính prefix sum để tính tổng nhanh
2. Lặp qua tất cả vị trí có thể đặt máy
3. Tìm lợi nhuận lớn nhất

Độ khó: Dễ (chỉ cần sliding window + prefix sum)
"""

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Tính prefix sum để tính tổng nhanh
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + A[i]

    max_profit = float('-inf')

    # Lặp qua tất cả vị trí có thể đặt máy (từ 0 đến N-K)
    for i in range(N - K + 1):
        # Tổng hút được từ vị trí i đến i+K-1
        sum_collected = prefix[i + K] - prefix[i]

        # Tính tổng bị cướp
        sum_lost = 0
        if i > 0:
            sum_lost += A[i - 1]
        if i + K < N:
            sum_lost += A[i + K]

        # Tính lợi nhuận
        profit = sum_collected - sum_lost
        max_profit = max(max_profit, profit)

    print(max_profit)

solve()
