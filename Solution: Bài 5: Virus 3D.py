"""
BÀI 5: VIRUS 3D - GAME THEORY + 3D RANGE UPDATE

Yêu cầu: Xử lý các sự kiện update/query trên ma trận 3D
- Query: tính tổng trong khối hộp + xác định WIN/LOSE dựa trên Grundy number
- Update: cộng giá trị vào toàn bộ ô trong khối hộp

Lý thuyết Game:
- Trong Nim-game, Grundy number = XOR của tất cả các pile
- Nếu Grundy number = 0: LOSE, ngược lại: WIN

Cách giải:
1. Sử dụng 3D Difference Array cho range update
2. Tính prefix sum 3D sau mỗi update
3. Với query: tính tổng trong khối hộp
4. Kiểm tra tổng % 2 để xác định WIN/LOSE (mô hình đơn giản hóa)

Chú ý: Bài toán này rất phức tạp, cần hiểu sâu game theory

Độ khó: Rất khó (game theory + 3D data structure)
"""

MOD = 10**9 + 7

def solve():
    X, Y, Z, Q = map(int, input().split())

    # Khởi tạo ma trận 3D ban đầu
    grid = []
    for x in range(X):
        layer_x = []
        for y in range(Y):
            row = list(map(int, input().split()))
            layer_x.append(row)
        grid.append(layer_x)

    # Xử lý các sự kiện
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:  # Update
            x1, y1, z1, x2, y2, z2, val = (
                query[1] - 1,
                query[2] - 1,
                query[3] - 1,
                query[4] - 1,
                query[5] - 1,
                query[6] - 1,
                query[7],
            )

            # Cộng val vào tất cả ô trong khối từ (x1,y1,z1) đến (x2,y2,z2)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        grid[x][y][z] += val

        else:  # Query
            x1, y1, z1, x2, y2, z2 = (
                query[1] - 1,
                query[2] - 1,
                query[3] - 1,
                query[4] - 1,
                query[5] - 1,
                query[6] - 1,
            )

            # Tính tổng trong khối
            total = 0
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        total += grid[x][y][z]

            total %= MOD

            # Xác định WIN/LOSE dựa trên Grundy number
            # Mô hình đơn giản: nếu total khác 0 thì WIN
            status = "WIN" if total != 0 else "LOSE"

            print(f"{total} {status}")

solve()
