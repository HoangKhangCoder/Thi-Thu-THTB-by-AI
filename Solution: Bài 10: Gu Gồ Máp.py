"""
BÀI 10: HỆ THỐNG ĐỊNH VỊ GU GỒ MÁP - TÌM ĐƯỜNG ĐI NGẮN NHẤT

Yêu cầu: Tìm đường đi ngắn nhất từ (x_start, y_start) đến (x_end, y_end)
trong đồ thị có trọng số

Cách giải:
- Sử dụng Dijkstra's Algorithm
- Các nút là các điểm tọa độ
- Các cạnh là các đường đi một chiều với trọng số là thời gian

Thuật toán Dijkstra:
1. Khởi tạo khoảng cách tất cả nút = vô cùng, ngoài trừ điểm bắt đầu = 0
2. Sử dụng priority queue (min-heap)
3. Mỗi lần lấy nút có khoảng cách nhỏ nhất chưa được thăm
4. Cập nhật khoảng cách của các nút kế tiếp
5. Lặp lại cho đến khi nút đích được thăm

Độ khó: Trung bình (cần hiểu Dijkstra's Algorithm)
"""

import heapq
from collections import defaultdict

def solve():
    V, E = map(int, input().split())
    x_start, y_start, x_end, y_end = map(int, input().split())

    # Xây dựng đồ thị
    graph = defaultdict(list)  # graph[(x1,y1)] = [(x2,y2,time), ...]

    for i in range(E):
        x1, y1, x2, y2, t = map(int, input().split())
        graph[(x1, y1)].append((x2, y2, t))

    # Dijkstra's Algorithm
    dist = {(x_start, y_start): 0}
    pq = [(0, x_start, y_start)]  # (distance, x, y)
    visited = set()

    while pq:
        d, x, y = heapq.heappop(pq)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        # Nếu đạt tới đích
        if x == x_end and y == y_end:
            print(d)
            return

        # Cập nhật khoảng cách của các nút kế tiếp
        for nx, ny, time in graph[(x, y)]:
            new_dist = d + time

            if (nx, ny) not in dist or new_dist < dist[(nx, ny)]:
                dist[(nx, ny)] = new_dist
                heapq.heappush(pq, (new_dist, nx, ny))

    # Nếu không tìm được đường đi
    print(-1)

solve()
