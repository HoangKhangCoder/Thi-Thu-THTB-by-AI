# Hệ Thống Định Vị "Gu Gồ Máp" Thời Đồ Đá (Bản Cập Nhật Siêu Kẹt Đường)

Vào kỷ Phấn Trắng năm $2026$, một cuộc khủng hoảng nghiêm trọng đã nổ ra tại thung lũng Gomora. Vì quá "đồ đá" và lạc hậu (chẳng khác gì anh bạn **Henry** từ thế kỷ $XVIII$ xuyên không về), hội khủng long ở đây hoàn toàn mù tịt đường đi lối lại và không biết cách sử dụng các ứng dụng hiện đại như Google Maps. Hậu quả là chúng liên tục đi lạc vào đầm lầy hoặc hang núi lửa.

Đứng trước tình cảnh đó, thiên tài công nghệ của bộ tộc — đại ca **T-Rex Cọc Cằn** — đã tự tay lập trình và phát triển một hệ thống định vị nội bộ mang tên **"Gu Gồ Máp"**. Bản đồ của T-Rex hoạt động trên một hệ lưới tọa độ nguyên. Có tổng cộng $V$ địa điểm quan trọng được đánh dấu bằng các cặp tọa độ $(x, y)$.

Để kết nối các địa điểm, T-Rex đã khảo sát và xây dựng $E$ tuyến đường một chiều. Tuy nhiên, các con đường thời đồ đá không hề bằng phẳng giống nhau: có đường đầy đá sỏi, có đường lại bị kẹt xe do bầy khủng long cổ dài đi bộ qua đường. Do đó, **mỗi con đường sẽ có một thời gian di chuyển $t$ hoàn toàn khác nhau**. Tuyến đường thứ $i$ sẽ dẫn trực tiếp từ địa điểm $(x_{1}, y_{1})$ đến địa điểm $(x_{2}, y_{2})$ và tốn đúng $t$ phút di chuyển. Vì đây là đường một chiều, khủng long chỉ có thể đi ngược lại nếu có một tuyến đường khác quy định cụ thể hướng ngược lại trong hệ thống.

Thanh niên **Tun Tung Tun Sahour** vốn cực kỳ cay cú T-Rex và luôn tìm cách dìm hàng anh chàng. Thế nhưng, trong một chuyến đi săn bắp cải ở vùng đất lạ, Tun Tung bị mất mạng (mất kết nối mạng $4G$ vũ trụ) và hoàn toàn mất phương hướng. Không còn cách nào khác, Tun Tung đành phải ngậm đắng nuốt cay mở ứng dụng **Gu Gồ Máp** của T-Rex lên để tìm đường sống.

Tun Tung Tun Sahour đang ở địa điểm nguồn $(x_{start}, y_{start})$ và muốn di chuyển đến địa điểm đích $(x_{end}, y_{end})$. Bạn hãy giúp thanh niên này tính toán xem **thời gian di chuyển ngắn nhất** là bao nhiêu phút? Nếu hệ thống đường một chiều đầy rẫy thời gian khác nhau của T-Rex không thể dẫn đến đích, hãy in ra $-1$ để Tun Tung chuẩn bị tinh thần dựng lều ngủ lại với bầy sói.

---

### Đầu vào (Standard Input)
- Dòng đầu tiên chứa hai số nguyên $V$ và $E$ ($2 \le V \le 1000$; $1 \le E \le 5000$) lần lượt là số lượng địa điểm và số lượng tuyến đường một chiều.
- Dòng thứ hai chứa 4 số nguyên $x_{start}, y_{start}, x_{end}, y_{end}$ biểu diễn tọa độ điểm xuất phát và điểm đích của Tun Tung Tun Sahour.
- $E$ dòng tiếp theo, dòng thứ $i$ chứa 5 số nguyên $x_{1}, y_{1}, x_{2}, y_{2}, t$ ($0 \le t \le 10^5$) mô tả một tuyến đường một chiều từ $(x_{1}, y_{1})$ đến $(x_{2}, y_{2})$ mất thời gian là $t$. Các giá trị $t$ của các con đường có thể hoàn toàn khác nhau tùy thuộc vào địa hình.

*(Dữ liệu đảm bảo các tọa độ $(x, y)$ trong file input đều là các số nguyên có giá trị tuyệt đối không vượt quá $10^9$ và nằm trong tập hợp $V$ địa điểm đã cho).*
*Nếu bạn thắc mắc T-Rex dễ thương là ai? Thì ở đây*
![T-Rex](https://cdn.chuyentin.net/ctoj/martor/db4934bc-1261-44ee-8c77-07307a7f924b.png)

---

### Đầu ra (Standard Output)
- In ra một số nguyên duy nhất là thời gian di chuyển ngắn nhất (tính bằng phút). Nếu không có đường đi, in ra $-1$.

---

### Giới hạn & Subtasks
- **Subtask 1 ($40\%$ số điểm):** $1 \le V \le 100$; $1 \le E \le 500$. Thời gian di chuyển của mỗi con đường $t$ nằm trong khoảng ($1 \le t \le 10$).
- **Subtask 2 ($60\%$ số điểm):** Không có giới hạn gì thêm ($2 \le V \le 1000$; $1 \le E \le 5000$; $0 \le t \le 10^5$).

---

### Ví dụ 1

#### Nhập vào:
```
4 4
1 1 4 4
1 1 2 2 12
2 2 4 4 35
1 1 3 3 5
3 3 4 4 18
```

#### In ra:
```
23
```

#### Giải thích ví dụ 1:
> Tun Tung muốn đi từ (1, 1) đến (4, 4). Các tuyến đường có thời gian t khác nhau rất rõ rệt:
> - Lộ trình 1: Từ (1, 1) -> (2, 2) -> (4, 4). Tổng thời gian: 12 + 35 = 47 phút.
> - Lộ trình 2: Từ (1, 1) -> (3, 3) -> (4, 4). Tổng thời gian: 5 + 18 = 23 phút.
>
> Thời gian ngắn nhất tìm được là 23 phút (chọn đi qua ngả (3, 3) cho đỡ “khủng long”).
