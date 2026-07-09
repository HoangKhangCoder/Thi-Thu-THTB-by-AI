# Virus "Sút-Nhầm-Gôn" Và Trận Chung Kết Sevastopol

Năm $2026$, do Trái Đất nóng lên làm tan chảy lớp băng vĩnh cửu tại Nam Cực, một chủng virus cổ đại có tên **"Virus Sút-Nhầm-Gôn" (Code-name: SNG-26)** đã thức giấc. Virus này sở hữu khả năng siêu nhiên: Bất kỳ siêu sao bóng đá nào nhiễm phải sẽ lập tức hóa thân thành "tiền vệ cho đội bạn".

Virus SNG-26 đã lây nhiễm vào Trạm Không Gian Trái Đất (Trạm Sevastopol) - nơi đang tổ chức trận Chung kết Giải Bóng đá Vũ trụ $3D$. Trạm được mô hình hóa thành một không gian $3D$ gồm các phòng có tọa độ $(x, y, z)$ với $1 \le x \le X$, $1 \le y \le Y$, $1 \le z \le Z$. Mỗi ô chứa một chỉ số lây nhiễm $V(x, y, z)$.

Do các phòng liên kết phức tạp qua hệ thống ống dẫn khí đa chiều, cấu trúc độc lập của mỗi vùng không gian $3D$ liên tục bị biến đổi bởi năng lượng của virus. Để dập dịch, hai kỹ sư Ethan Hunt và Cầu thủ X phải tham gia một trò chơi đối kháng điều khiển Robot diệt khuẩn trên mạng lưới $3D$:

1. Ban đầu, Robot nằm tại vị trí xuất phát $(1, 1, 1)$.
2. Hai người chơi lượt lượt di chuyển Robot sang các ô lân cận theo các hướng ống dẫn khí cho phép trên ma trận $3D$.
3. Khi Robot di chuyển qua các khu vực, năng lượng của nó sẽ kích hoạt tính năng làm thay đổi chỉ số lây nhiễm của một **khối hộp không gian $3D$** từ $(x_1, y_1, z_1)$ đến $(x_2, y_2, z_2)$.
4. Một vùng không gian được xem là "An toàn" nếu tổng chỉ số lây nhiễm tích lũy thuộc tập giá trị Grundy chiến thắng (thỏa mãn quy tắc Nim-sum của đồ thị $3D$).
5. Người chơi nào bị đẩy vào vị trí mà Robot không thể tiếp tục di chuyển hoặc rơi vào vùng có tổng chỉ số lây nhiễm bất lợi sẽ thua cuộc và chính thức trở thành **"tiền vệ cho đội bạn"**.

Bạn hãy viết chương trình xử lý chuỗi $Q$ sự kiện biến đổi không gian và truy vấn trạng thái trò chơi trên trạm Sevastopol.

---

### Đầu vào
- Dòng đầu tiên chứa $4$ số nguyên $X, Y, Z, Q$ ($1 \le X, Y, Z \le 100$, $1 \le Q \le 10^5$).
- Tiếp theo là $X \times Y$ dòng, mỗi dòng chứa $Z$ số nguyên biểu diễn chỉ số lây nhiễm ban đầu $V(x, y, z)$.
- $Q$ dòng tiếp theo, mỗi dòng biểu diễn một sự kiện thuộc một trong hai dạng:
  - `1 x1 y1 z1 x2 y2 z2 val`: Robot phát luồng năng lượng làm thay đổi chỉ số lây nhiễm của toàn bộ các ô trong khối hộp từ $(x_1, y_1, z_1)$ đến $(x_2, y_2, z_2)$ một lượng `val` (Cập nhật Mảng hiệu $3D$).
  - `2 x1 y1 z1 x2 y2 z2`: Truy vấn tổng chỉ số lây nhiễm trong khối hộp từ $(x_1, y_1, z_1)$ đến $(x_2, y_2, z_2)$ và kiểm tra trạng thái lượt đi của trò chơi tại vùng này.

---

### Đầu ra
- Với mỗi sự kiện loại $2$, in ra trên một dòng gồm hai thông tin cách nhau bởi dấu khoảng trắng:
  - Tổng chỉ số lây nhiễm trong khối hộp (chia lấy dư cho $10^9 + 7$).
  - Trạng thái lượt đi của người chơi hiện tại: `WIN` (nếu có chiến thuật thắng) hoặc `LOSE` (nếu cầm chắc thất bại và trở thành "tiền vệ cho đội bạn").

> [!NOTE]
> Thời gian tối đa: $2$ s
> 
> Bộ nhớ tối đa: $512$ MB

---

### Giới hạn & Subtasks
- **Subtask 1 ($20\%$ số điểm):** $1 \le X, Y, Z \le 10$; $Q \le 100$.
- **Subtask 2 ($30\%$ số điểm):** $1 \le X, Y, Z \le 40$; $Q \le 5000$.
- **Subtask 3 ($50\%$ số điểm):** $1 \le X, Y, Z \le 100$; $Q \le 10^5$.

---

### Ví dụ 1

#### Nhập vào:
```
2 2 2 2
1 2
3 4
5 6
7 8
1 1 1 1 2 2 2 5
2 1 1 1 2 2 2
```

#### In ra:
```
76 WIN
```

#### Giải thích ví dụ 1:
- Khối không gian $2 \times 2 \times 2$ ban đầu có tổng chỉ số lây nhiễm $= 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36$.
- Sự kiện $1$: Cộng thêm `val = 5` vào tất cả $8$ ô trong khối từ $(1, 1, 1)$ đến $(2, 2, 2)$. Tổng chỉ số cộng thêm $= 8 \times 5 = 40$.
- Sự kiện $2$: Tổng chỉ số lây nhiễm mới $= 36 + 40 = 76$. Giá trị Trò chơi (Grundy value) của vùng này khác $0$, do đó người chơi ở lượt đi hiện tại đạt trạng thái `WIN`.
