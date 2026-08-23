"""
BÀI 9: KỶ LỤC ĐỈNH CAO - TÍNH THỂ TÍCH KHÔNG BỊ PHỦ (3D)

Yêu cầu: Tính số ô 3D không bị phủ bởi bất kỳ hộp nào

Cách giải (Coordinate Compression 3D):
1. Nén tọa độ x, y, z
2. Tạo bảng 3D nén
3. Đánh dấu các ô bị phủ
4. Tính thể tích thực tế

Phương pháp:
- Tương tự bài 8 nhưng mở rộng lên 3D
- Thay vì hình chữ nhật 2D, dùng hộp 3D
- Tính thể tích = width * height * depth

Độ khó: Khó (coordinate compression 3D phức tạp)
"""

def solve():
    N, X, Y, Z = map(int, input().split())
    boxes = []
    for i in range(N):
        x1, y1, z1, x2, y2, z2 = map(int, input().split())
        boxes.append((x1, y1, z1, x2, y2, z2))

    # Thu thập tất cả tọa độ
    xs = set([1, X + 1])
    ys = set([1, Y + 1])
    zs = set([1, Z + 1])

    for x1, y1, z1, x2, y2, z2 in boxes:
        xs.add(x1)
        xs.add(x2 + 1)
        ys.add(y1)
        ys.add(y2 + 1)
        zs.add(z1)
        zs.add(z2 + 1)

    xs = sorted(list(xs))
    ys = sorted(list(ys))
    zs = sorted(list(zs))

    # Tạo bảng 3D nén
    grid = [
        [[False] * (len(zs) - 1) for _ in range(len(ys) - 1)]
        for _ in range(len(xs) - 1)
    ]

    # Đánh dấu các ô bị phủ
    for x1, y1, z1, x2, y2, z2 in boxes:
        x1_idx = xs.index(x1)
        x2_idx = xs.index(x2 + 1)
        y1_idx = ys.index(y1)
        y2_idx = ys.index(y2 + 1)
        z1_idx = zs.index(z1)
        z2_idx = zs.index(z2 + 1)

        for i in range(x1_idx, x2_idx):
            for j in range(y1_idx, y2_idx):
                for k in range(z1_idx, z2_idx):
                    grid[i][j][k] = True

    # Tính thể tích bị phủ
    covered = 0
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            for k in range(len(zs) - 1):
                if grid[i][j][k]:
                    width = xs[i + 1] - xs[i]
                    height = ys[j + 1] - ys[j]
                    depth = zs[k + 1] - zs[k]
                    covered += width * height * depth

    # Thể tích còn lại
    total = X * Y * Z
    result = total - covered
    print(result)

solve()
