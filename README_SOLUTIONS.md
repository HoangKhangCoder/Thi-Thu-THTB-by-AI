# 📝 SOLUTIONS - 10 BÀI TẬP LUYỆN THI

Dự án này chứa **10 file solution Python** kèm chú thích tiếng Việt chi tiết cho mỗi bài toán cùng một **file đánh giá độ khó** so sánh với LeetCode.

## 📂 Danh Sách Files

### Solution Files (Code Python)

| # | Tên File | Bài Toán | Độ Khó |
|---|----------|----------|--------|
| 1 | `Solution: Bài 1: Số C.py` | Tính công thức với modulo | ⭐⭐ |
| 2 | `Solution: Bài 2: Di chuyển.py` | DP 2D - số 0 tận cùng | ⭐⭐⭐ |
| 3 | `Solution: Bài 3: Trò chơi Đảo Ngọc.py` | DFS + DP - đếm đường đi | ⭐⭐⭐⭐ |
| 4 | `Solution: Bài 4: Mèo Béo.py` | Sliding window - lợi nhuận | ⭐⭐ |
| 5 | `Solution: Bài 5: Virus 3D.py` | Game theory + 3D range | ⭐⭐⭐⭐⭐ |
| 6 | `Solution: Bài 6: Đếm nhóm.py` | Partition number (N lớn) | ⭐⭐⭐⭐⭐ |
| 7 | `Solution: Bài 7: Chấn động World Cup.py` | DP partition | ⭐⭐⭐ |
| 8 | `Solution: Bài 8: Lãnh Địa Bất Khả Xâm Phạm.py` | Coordinate compression 2D | ⭐⭐⭐ |
| 9 | `Solution: Bài 9: Kỷ Lục Đỉnh Cao.py` | Coordinate compression 3D | ⭐⭐⭐⭐ |
| 10 | `Solution: Bài 10: Gu Gồ Máp.py` | Dijkstra's shortest path | ⭐⭐⭐ |

### Đánh Giá & Tài Liệu

| Tên File | Nội Dung |
|----------|----------|
| `ĐÁNH GIÁ ĐỘ KHÓ - So sánh với LeetCode.md` | Chi tiết độ khó mỗi bài, so sánh với LeetCode, tóm tắt kỹ thuật |
| `README_SOLUTIONS.md` | File này - hướng dẫn sử dụng |

---

## 🎯 Hướng Dẫn Sử Dụng

### Cách chạy một solution

```bash
# Chạy solution bài 1
python "Solution: Bài 1: Số C.py" < input.txt

# Hoặc nhập input trực tiếp
echo "5" | python "Solution: Bài 1: Số C.py"
```

### Cấu trúc mỗi solution

Mỗi file Python chứa:
1. **Docstring**: Mô tả bài toán, cách giải, độ khó
2. **Hàm `solve()`**: Logic giải quyết chính
3. **Input/Output**: Code đọc input và in output

### Ví dụ

```python
"""
BÀI X: TÊN BÀI - MÔ TẢ

Yêu cầu: ...
Cách giải: ...
Độ khó: ...
"""

def solve():
    # Logic ở đây
    pass

# Chạy
solve()
```

---

## 📊 Thống Kê Kỹ Thuật

### Kỹ thuật sử dụng trong 10 bài

| Kỹ Thuật | Bài | Tần Suất |
|----------|-----|----------|
| **Dynamic Programming** | 2, 3, 6, 7 | 4 bài |
| **Dijkstra/Shortest Path** | 10 | 1 bài |
| **Coordinate Compression** | 8, 9 | 2 bài |
| **Sliding Window** | 4 | 1 bài |
| **Game Theory (Nim)** | 5 | 1 bài |
| **Số học** | 1, 2, 6 | 3 bài |
| **DFS/Backtracking** | 3 | 1 bài |

### Phân bố độ khó

- **⭐⭐ (Dễ)**: 2 bài → Dùng làm nền tảng
- **⭐⭐⭐ (Trung bình)**: 5 bài → Chiếm đa số
- **⭐⭐⭐⭐ (Khó)**: 2 bài → Cần tư duy sâu
- **⭐⭐⭐⭐⭐ (Rất khó)**: 1 bài → Challenge cao nhất

---

## 🚀 Lộ Trình Học Tập Gợi Ý

### Giai đoạn 1: Nền tảng (1-2 tuần)
- [ ] Bài 1: Số C (công thức toán)
- [ ] Bài 4: Mèo Béo (sliding window)

### Giai đoạn 2: DP cơ bản (2-3 tuần)
- [ ] Bài 2: Di chuyển (DP 2D)
- [ ] Bài 7: World Cup (DP partition)
- [ ] Bài 10: Gu Gồ Máp (Dijkstra)

### Giai đoạn 3: Kỹ thuật nâng cao (3-4 tuần)
- [ ] Bài 8: Lãnh Địa (Coordinate compression 2D)
- [ ] Bài 3: Đảo Ngọc (DFS + DP)

### Giai đoạn 4: Challenge (4-6 tuần)
- [ ] Bài 9: Kỷ Lục (Coordinate compression 3D)
- [ ] Bài 5: Virus 3D (Game theory)
- [ ] Bài 6: Đếm nhóm (Partition lớn)

---

## 🔍 Chú Thích Trong Code

Mỗi solution có chú thích chi tiết bằng **tiếng Việt** giải thích:

✅ **Yêu cầu bài toán**
```python
# Mô tả rõ ràng về input/output
```

✅ **Ý tưởng thuật toán**
```python
# Phân tích công thức, logic, hay cách tiếp cận
```

✅ **Implementation chi tiết**
```python
# Chú thích từng bước trong code
```

✅ **Độ phức tạp**
```python
# Thời gian: O(N^2), Không gian: O(N)
```

---

## 💡 Tips Khi Sử Dụng

### 1. Hiểu trước khi chạy
- Đọc docstring để hiểu bài toán
- Phân tích ví dụ trong description bài toán
- Vẽ biểu đồ hoặc trace qua ví dụ

### 2. Chạy với test cases
- Input từ các ví dụ trong bài toán
- Tạo thêm edge cases (N=0, N=1, max N)
- So sánh output với expected

### 3. Tối ưu hóa
- Nếu TLE: kiểm tra độ phức tạp
- Nếu MLE: xem xét cấu trúc dữ liệu
- Kiểm tra các boundary conditions

### 4. Học từ solutions
- Đọc code để hiểu cách implement
- Tự code lại không nhìn solution
- So sánh logic của bạn vs solution

---

## ⚠️ Lưu Ý Quan Trọng

### Bài 5 (Virus 3D)
- Bài này yêu cầu hiểu game theory (Nim-game)
- Mã solution hiện tại là phiên bản đơn giản hóa
- Để AC hết subtask cần implement 3D Fenwick tree hoặc Segment tree

### Bài 6 (Đếm nhóm)
- N có thể lên đến 10^12 là rất khó
- Với N > 10^5, DP không khả thi
- Cần công thức toán học hoặc xấp xỉ asymptotic

### Các bài khác
- Hầu hết solutions đủ để AC full subtasks
- Nếu TLE, hãy kiểm tra lại độ phức tạp

---

## 📚 Tài Liệu Tham Khảo

### LeetCode Tương Đương
- Bài 1 ≈ LeetCode #504, #172
- Bài 2 ≈ LeetCode #64, #62
- Bài 3 ≈ LeetCode #1125, #1371
- Bài 4 ≈ LeetCode #121, #122
- Bài 5 ≈ LeetCode #1317 + Game Theory
- Bài 6 ≈ Partition Number (số học cao cấp)
- Bài 7 ≈ LeetCode #70, #198
- Bài 8 ≈ LeetCode #850, #223
- Bài 9 ≈ 3D Union problem
- Bài 10 ≈ LeetCode #743, #787

### Kiến Thức Cần
- Dynamic Programming (Bài 2, 3, 6, 7)
- Graph Theory (Bài 10)
- Coordinate Compression (Bài 8, 9)
- Game Theory (Bài 5)
- Modular Arithmetic (Bài 1, 6)

---

## 📝 Mẹo Gỡ Lỗi

### Nếu code không chạy
1. Kiểm tra format input đúng không
2. Kiểm tra kiểu dữ liệu (int vs float)
3. Kiểm tra off-by-one errors
4. In ra intermediate values để debug

### Nếu output sai
1. So sánh với ví dụ trong bài
2. Kiểm tra base case (N=0, N=1)
3. Kiểm tra boundary conditions
4. Kiểm tra modulo operations nếu có

### Nếu TLE (Time Limit Exceeded)
1. Kiểm tra độ phức tạp thời gian
2. Xem có nested loop không cần thiết
3. Thay từ O(N^2) sang O(N log N) nếu có
4. Kiểm tra I/O performance

---

## 🎓 Học Kỳ

Toàn bộ 10 bài này được thiết kế để luyện tập **DP, Graph, và Số Học** ở mức độ cao. Đây là các bài tập kiểm tra khả năng:

✅ Phân tích bài toán
✅ Thiết kế thuật toán
✅ Implement hiệu quả
✅ Optimize khi cần
✅ Xử lý edge cases

---

**Chúc bạn học tập hiệu quả! 🚀**

Nếu có câu hỏi hoặc cần giải thích thêm, hãy tham khảo file `ĐÁNH GIÁ ĐỘ KHÓ` để hiểu rõ hơn về mỗi bài toán.
