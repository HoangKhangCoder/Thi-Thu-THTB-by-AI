"""
BÀI 1: SỐ C - TÍNH CÔNG THỨC TOÁN HỌC VỚI MODULO

Yêu cầu: Tính C_N với công thức đệ quy
- A_i = A_{i-1} + 2
- B_i = B_{i-1} + A_i
- C_i = C_{i-1} + B_i
- Kết quả: C_N mod (10^9 + 7)

Phân tích:
- A_N = 2*N (cấp số cộng)
- B_N = 2 + 4 + 6 + ... + 2*N = N*(N+1) (tổng số chẵn)
- C_N = tổng của B từ 1 đến N = N*(N+1)*(N+2)/3

Độ khó: Dễ (chỉ cần công thức toán học)
"""

MOD = 10**9 + 7

def mod_inverse(a, mod):
    # Tính modular inverse bằng Fermat's Little Theorem
    return pow(a, mod - 2, mod)

def solve(N):
    N = N % MOD
    # C_N = N * (N+1) * (N+2) / 3
    numerator = (N * (N + 1) % MOD) * (N + 2) % MOD
    result = numerator * mod_inverse(3, MOD) % MOD
    return result

N = int(input())
print(solve(N))
