# ĐÁNH GIÁ ĐỘ KHÓ 10 BÀI VỚI LEETCODE

## Bảng Tóm Tắt

| Bài | Tên Bài | Độ Khó | LeetCode Tương Đương | Lý Do |
|-----|---------|--------|----------------------|-------|
| 1 | Số C | ⭐⭐ (Dễ) | Easy | Chỉ cần công thức toán học |
| 2 | Di chuyển | ⭐⭐⭐ (Trung bình) | Medium | DP 2D + tính thừa số nguyên tố |
| 3 | Trò chơi Đảo Ngọc | ⭐⭐⭐⭐ (Khó) | Hard | DFS + DP kết hợp, logic phức tạp |
| 4 | Mèo Béo | ⭐⭐ (Dễ) | Easy | Sliding window + prefix sum |
| 5 | Virus 3D | ⭐⭐⭐⭐⭐ (Rất Khó) | Hard | Game theory Nim + 3D data structure |
| 6 | Đếm nhóm | ⭐⭐⭐⭐⭐ (Rất Khó) | Hard | Partition number với N lên đến 10^12 |
| 7 | Chấn động World Cup | ⭐⭐⭐ (Trung bình) | Medium | DP partition, N lên đến 10^5 |
| 8 | Lãnh Địa Bất Khả Xâm Phạm | ⭐⭐⭐ (Trung bình) | Medium | Coordinate compression 2D |
| 9 | Kỷ Lục Đỉnh Cao | ⭐⭐⭐⭐ (Khó) | Hard | Coordinate compression 3D |
| 10 | Gu Gồ Máp | ⭐⭐⭐ (Trung bình) | Medium | Dijkstra's shortest path |

---

## Chi Tiết Từng Bài

### 📍 Bài 1: Số C - ⭐⭐ (DỄ)

**Độ khó LeetCode:** Easy (Tương đương: LeetCode #1, #9, #13)

**Phân tích:**
- Chỉ cần tìm công thức toán học: `C_N = N*(N+1)*(N+2)/3`
- Có thể giải bằng phép tính trực tiếp
- Thách thức duy nhất: xử lý modular arithmetic đúng cách

**Điểm mạnh/yếu:**
- ✅ Không cần cấu trúc dữ liệu phức tạp
- ✅ Thời gian: O(1)
- ❌ Cần hiểu về modular inverse

**So sánh:** Dễ hơn LeetCode Medium, sánh với LeetCode Easy

---

### 📍 Bài 2: Di chuyển - ⭐⭐⭐ (TRUNG BÌNH)

**Độ khó LeetCode:** Medium (Tương đương: LeetCode #62, #63, #64)

**Phân tích:**
- DP 2D cơ bản với twist: tính thừa số nguyên tố (2 và 5)
- Phải hiểu rằng: số 0 tận cùng = min(count_2, count_5)
- Xử lý case 0 khó khăn hơn

**Điểm mạnh/yếu:**
- ✅ DP quen thuộc
- ✅ Threshold dễ nhận ra
- ❌ Cần tính toán saoban số nguyên tố
- ❌ Case 0 phức tạp (trả về ∞ hoặc không)

**So sánh:** Tương đương LeetCode Medium

---

### 📍 Bài 3: Trò chơi Đảo Ngọc - ⭐⭐⭐⭐ (KHÓ)

**Độ khó LeetCode:** Hard (Tương đương: LeetCode #1125, #1371)

**Phân tích:**
- Kết hợp DFS + DP
- Phải tính cả số lượng đường đi + max sum cùng một lúc
- Ràng buộc tọa độ tăng làm logic phức tạp

**Điểm mạnh/yếu:**
- ✅ Ý tưởng rõ ràng: DFS tìm tất cả đường đi
- ❌ Cần theo dõi 2 metric (count + sum)
- ❌ Cần theo dõi tính chẵn/lẻ của sum
- ❌ Backtracking có thể TLE nếu không tối ưu

**So sánh:** Khó hơn LeetCode Medium, sánh với LeetCode Hard

---

### 📍 Bài 4: Mèo Béo - ⭐⭐ (DỄ)

**Độ khó LeetCode:** Easy (Tương đương: LeetCode #121, #122, #123)

**Phân tích:**
- Bài toán sliding window + prefix sum
- Chỉ cần lặp qua tất cả vị trí có thể
- Không có tối ưu phức tạp

**Điểm mạnh/yếu:**
- ✅ Rất đơn giản: O(N)
- ✅ Không cần cấu trúc dữ liệu
- ❌ Dễ dàng "off-by-one" với các boundary case

**So sánh:** Sánh với LeetCode Easy

---

### 📍 Bài 5: Virus 3D - ⭐⭐⭐⭐⭐ (RẤT KHÓ)

**Độ khó LeetCode:** Hard+ (Tương đương: LeetCode #1157, #1317 + Game Theory)

**Phân tích:**
- Game theory (Grundy number, Nim-game)
- 3D range update/query
- Cần hiểu sâu về impartial games

**Điểm mạnh/yếu:**
- ✅ Ý tưởng game theory thú vị
- ❌ Rất khó hiểu nếu chưa học game theory
- ❌ Cần implement 3D difference array hoặc 3D Fenwick tree
- ❌ Tính toán Grundy value phức tạp

**So sánh:** Khó hơn LeetCode Hard, cần knowledge về game theory

---

### 📍 Bài 6: Đếm nhóm - ⭐⭐⭐⭐⭐ (RẤT KHÓ)

**Độ khó LeetCode:** Hard+ (Tương đương: LeetCode #356 hoặc bài toán số học cao cấp)

**Phân tích:**
- Tính "Partition Number" p(N)
- N lên đến 10^12 là điểm khó khăn chính
- Subtask cuối yêu cầu công thức toán học cao cấp hoặc xấp xỉ

**Điểm mạnh/yếu:**
- ✅ DP cơ bản dễ làm cho N nhỏ
- ❌ Với N > 10^5, cần kỹ thuật không trivial
- ❌ Bài toán yêu cầu "trả lời Bi" nếu là LLM (gợi ý là bài rất khó)
- ❌ Cần hiểu công thức Euler hoặc xấp xỉ asymptotic

**So sánh:** Khó hơn LeetCode Hard, cần kiến thức toán cao cấp

---

### 📍 Bài 7: Chấn động World Cup - ⭐⭐⭐ (TRUNG BÌNH)

**Độ khó LeetCode:** Medium (Tương đương: LeetCode #70, #198, #213)

**Phân tích:**
- Tính Partition Number với N lên đến 10^5 là vừa phải
- DP: `dp[n][k] = số cách phân hoạch n dùng số ≤ k`
- Công thức: `dp[n][k] = dp[n][k-1] + dp[n-k][k]`

**Điểm mạnh/yếu:**
- ✅ DP rõ ràng và tối ưu
- ✅ Có thể hiểu được với DP cơ bản
- ✅ Thời gian: O(N^2)
- ❌ Cần hiểu công thức DP partition

**So sánh:** Tương đương LeetCode Medium

---

### 📍 Bài 8: Lãnh Địa Bất Khả Xâm Phạm - ⭐⭐⭐ (TRUNG BÌNH)

**Độ khó LeetCode:** Medium (Tương đương: LeetCode #850, #223)

**Phân tích:**
- Coordinate compression 2D
- Tính diện tích hợp của các hình chữ nhật
- Có thể dùng sweep line hoặc coordinate compression

**Điểm mạnh/yếu:**
- ✅ Ý tưởng coordinate compression rất elegant
- ✅ Dễ implement một khi hiểu ý tưởng
- ❌ Cần hiểu sâu về coordinate compression
- ❌ Dễ lỗi với boundary conditions

**So sánh:** Tương đương LeetCode Medium

---

### 📍 Bài 9: Kỷ Lục Đỉnh Cao - ⭐⭐⭐⭐ (KHÓ)

**Độ khó LeetCode:** Hard (Tương đương: LeetCode #3D Union, Advanced Geometry)

**Phân tích:**
- Coordinate compression 3D
- Mở rộng 2D lên 3D khó khăn gấp 3 lần
- Cần hiểu cách nén tọa độ cho 3 chiều

**Điểm mạnh/yếu:**
- ✅ Ý tưởng tương tự bài 8 nhưng mở rộng
- ✅ Thú vị với 3D geometry
- ❌ Cấu trúc 3D phức tạp hơn rất nhiều
- ❌ Dễ gặp lỗi index khi làm việc với 3D
- ❌ Memory overhead lớn hơn

**So sánh:** Khó hơn LeetCode Medium, sánh với LeetCode Hard

---

### 📍 Bài 10: Gu Gồ Máp - ⭐⭐⭐ (TRUNG BÌNH)

**Độ khó LeetCode:** Medium (Tương đương: LeetCode #743, #787, #1334)

**Phân tích:**
- Dijkstra's Algorithm kinh điển
- Cách xây dựng đồ thị từ tọa độ hơi khác một chút
- Có thể TLE nếu không tối ưu

**Điểm mạnh/yếu:**
- ✅ Dijkstra quen thuộc
- ✅ Có thể dùng heapq sẵn có của Python
- ✅ Thời gian: O((V+E)logV) với priority queue
- ❌ Cần hiểu cách xây dựng adjacency list từ tọa độ

**So sánh:** Tương đương LeetCode Medium

---

## 📊 Tóm Tắt Thống Kê

### Phân bố độ khó:

| Mức | Số lượng | Bài |
|-----|----------|-----|
| ⭐⭐ | 2 | Bài 1, 4 |
| ⭐⭐⭐ | 4 | Bài 2, 7, 8, 10 |
| ⭐⭐⭐⭐ | 2 | Bài 3, 9 |
| ⭐⭐⭐⭐⭐ | 2 | Bài 5, 6 |

**Trung bình:** ⭐⭐⭐ ~ ⭐⭐⭐⭐ (Trung bình đến khó)

### So sánh với LeetCode:

- **LeetCode Easy:** 2 bài (Bài 1, 4)
- **LeetCode Medium:** 4 bài (Bài 2, 7, 8, 10)
- **LeetCode Hard:** 2 bài (Bài 3, 9)
- **LeetCode Hard+:** 2 bài (Bài 5, 6)

---

## 🎯 Bài Toán Yêu Thích (Challenge Ranking)

1. **Bài 5 (Virus 3D)** - Game theory + 3D, rất thách thức
2. **Bài 6 (Đếm nhóm)** - Partition number với N lớn, toán học cao cấp
3. **Bài 9 (Kỷ Lục Đỉnh Cao)** - Coordinate compression 3D, elegant
4. **Bài 3 (Trò chơi Đảo Ngọc)** - DFS + DP, logic phức tạp

---

## 💡 Kinh Nghiệm Rút Ra

### Các kỹ thuật quan trọng:
1. **DP** - Bài 2, 3, 6, 7
2. **Dijkstra** - Bài 10
3. **Coordinate Compression** - Bài 8, 9
4. **Sliding Window** - Bài 4
5. **Game Theory** - Bài 5
6. **Số học** - Bài 1, 6

### Thứ tự học tập recommend:
1. Bài 1, 4 (nền tảng)
2. Bài 2, 10 (DP + Dijkstra cơ bản)
3. Bài 7, 8 (DP partition + coordinate compression)
4. Bài 3, 9 (DFS + 3D)
5. Bài 5, 6 (game theory + số học cao cấp)
