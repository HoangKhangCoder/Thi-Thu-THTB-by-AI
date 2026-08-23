"""
BÀI 8: LÃNH ĐỊA BẤT KHẢ XÂM PHẠM - TÍNH DIỆN TÍCH KHÔNG BỊ PHỦ

Yêu cầu: Tính số ô không bị phủ bởi bất kỳ hình chữ nhật nào

Cách giải:
1. Tính tổng diện tích = M * K
2. Tính tổng diện tích bị phủ bằng Inclusion-Exclusion
3. Diện tích còn lại = Tổng - Diện tích bị phủ

Phương pháp Coordinate Compression:
- Nén tọa độ x: chỉ giữ các tọa độ quan trọng
- Nén tọa độ y: chỉ giữ các tọa độ quan trọng
- Tạo bảng 2D nhỏ hơn
- Đánh dấu các ô bị phủ trong bảng nén
- Tính lại diện tích thực

Độ khó: Trung bình (cần hiểu coordinate compression)
"""

def solve():
    N, M, K = map(int, input().split())
    rectangles = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append((x1, y1, x2, y2))

    # Collect all x and y coordinates
    xs = set([1, M + 1])
    ys = set([1, K + 1])

    for x1, y1, x2, y2 in rectangles:
        xs.add(x1)
        xs.add(x2 + 1)
        ys.add(y1)
        ys.add(y2 + 1)

    xs = sorted(list(xs))
    ys = sorted(list(ys))

    # Tạo bảng nén
    grid = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]

    # Đánh dấu các ô bị phủ
    for x1, y1, x2, y2 in rectangles:
        x1_idx = xs.index(x1)
        x2_idx = xs.index(x2 + 1)
        y1_idx = ys.index(y1)
        y2_idx = ys.index(y2 + 1)

        for i in range(x1_idx, x2_idx):
            for j in range(y1_idx, y2_idx):
                grid[i][j] = True

    # Tính diện tích bị phủ
    covered = 0
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            if grid[i][j]:
                width = xs[i + 1] - xs[i]
                height = ys[j + 1] - ys[j]
                covered += width * height

    # Diện tích còn lại
    total = M * K
    result = total - covered
    print(result)

solve()
