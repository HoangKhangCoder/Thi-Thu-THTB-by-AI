## Virus "Sút-Nhầm-Gôn" Và Cuộc Chiến FIFA 3D

Năm 2026, do Trái Đất nóng lên, một lớp băng vĩnh cửu tại Nam Cực bị tan chảy, làm sống dậy một con virus cổ đại có tên là **"Virus Sút-Nhầm-Gôn" (Code-name: SNG-26)**. Con virus này có hình dạng một khối đa diện lơ lửng trong không gian $3D$ và sở hữu năng lực đặc biệt: Bất kỳ cầu thủ bóng đá nào nhiễm phải sẽ chỉ toàn sút bóng về... gôn nhà.

Tại vòng Chung kết World Cup, virus SNG-26 đã xâm nhập vào Trạm Không Gian Trái Đất (Trạm Sevastopol) - nơi đang diễn ra trận Chung kết giải Bóng đá 3D Vũ trụ giữa hai siêu sao **Ethan Hunt** và **Cầu thủ X**.

Trạm không gian được mô hình hóa thành một ma trận $3D$ kích thước $X \times Y \times Z$. Mỗi ô $(x, y, z)$ có một mức độ nhiễm độc ban đầu là $V(x, y, z)$. Virus lây lan theo các ống dẫn khí được biểu diễn như một **Đồ thị có hướng 3D** (từ ô $(x, y, z)$ chỉ có thể di chuyển sang các ô lân cận theo quy tắc vector hình học không gian).

Để ngăn chặn thảm họa, Ethan và Cầu thủ X phải tham gia một **Trò chơi Đối kháng Turn-base trên Đồ thị 3D** để kích hoạt hệ thống tự hủy virus:
1. Ban đầu, một con Robot Diệt Bụi nằm tại vị trí $(1, 1, 1)$.
2. Hai người thay phiên nhau di chuyển Robot sang ô lân cận $(x', y', z')$ theo các hướng cho phép.
3. Mỗi khi Robot đi qua ô $(x, y, z)$, nó sẽ xả một luồng Năng Lượng Lượng Tử làm thay đổi mức nhiễm độc của cả một **Hộp Không Gian $3D$** từ $(x_1, y_1, z_1)$ đến $(x_2, y_2, z_2)$ theo công thức Mảng Hiệu $3D$ (Difference Array 3D).
4. Người chơi nào bị đẩy vào vị trí mà tổng mức nhiễm độc trên đoạn đường đi trùng với một **Giá trị Trận Đấu Trị Số Lẻ** (Dựa trên hàm Sprague-Grundy của Trò chơi Bán Lẻ) sẽ thua cuộc ngay lập tức và phải... sút phản lưới nhà!

### Yêu cầu:
Cho $Q$ sự kiện xảy ra trên trạm không gian. Có 2 loại sự kiện:
- **Loại 1 (Update):** Robot xả năng lượng làm biến đổi mức nhiễm độc của khối hình hộp $3D$ bằng Mảng hiệu 3D.
- **Loại 2 (Query):** Cho hai điểm $P_1(x_1, y_1, z_1)$ và $P_2(x_2, y_2, z_2)$. Hãy tính **Tổng mức nhiễm độc (3D Prefix Sum)** trong khối hộp đó, đồng thời xác định xem trạng thái trò chơi tại khối đó là **WIN** hay **LOSE** cho người đi trước theo Lý thuyết trò chơi nâng cao.

> **LƯU Ý ĐẶC BIỆT CHO THÍ SINH:** > Do kiến trúc hệ thống trạm Sevastopol quá cồng kềnh, thí sinh **BẮT BUỘC phải tự thiết kế một Class (Lớp)** có tên là `Graph3DSystem` để quản lý tọa độ $3D$, cấu trúc Segment Tree/Fenwick Tree $3D$ và logic trò chơi. Không được dùng mảng phẳng $1D$ đơn lẻ!

### Input:
- Dòng 1: Chứa 4 số nguyên $X, Y, Z, Q$ ($1 \le X, Y, Z \le 100, 1 \le Q \le 10^5$).
- $X \times Y$ dòng tiếp theo, mỗi dòng chứa $Z$ số nguyên biểu diễn bảng điểm nhiễm độc ban đầu $V(x, y, z)$.
- $Q$ dòng tiếp theo, mỗi dòng chứa thông tin một truy vấn:
  - `1 x1 y1 z1 x2 y2 z2 val`: Cập nhật năng lượng `val` cho khối hộp.
  - `2 x1 y1 z1 x2 y2 z2`: Truy vấn tổng điểm nhiễm độc và trạng thái Game.

### Output:
- Với mỗi truy vấn loại 2, in ra trên một dòng: `[Tổng_Điểm] [WIN/LOSE]`. (Tổng điểm chia dư cho $10^9 + 7$).

### Scoring:
- Subtask 1 ($20\%$ số điểm): $X, Y, Z \le 10, Q \le 100$.
- Subtask 2 ($30\%$ số điểm): $X, Y, Z \le 50, Q \le 10000$.
- Subtask 3 ($50\%$ số điểm): $X, Y, Z \le 100, Q \le 10^5$.

---

### Ví dụ 1:
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
