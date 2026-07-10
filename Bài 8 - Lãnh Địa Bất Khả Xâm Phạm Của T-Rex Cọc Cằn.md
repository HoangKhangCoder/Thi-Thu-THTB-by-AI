# Lãnh Địa Bất Khả Xâm Phạm Của T-Rex Cọc Cằn

Tại thung lũng Gomora năm $2026$, đại ca **T-Rex Cọc Cằn** đang vô cùng tức giận. Chuyện là anh chàng vừa tậu một miếng đất hình chữ nhật siêu to khổng lồ có kích thước $M \times K$ ô đơn vị để làm nơi nằm ườn và gặm cỏ bắp cải (T-Rex này ăn chay). Hệ tọa độ của miếng đất có góc trái dưới là $(1, 1)$ và góc phải trên là $(M, K)$.

Tuy nhiên, thung lũng này còn có sự xuất hiện của $N$ con khủng long tí hon ăn chực khác (đứng đầu là thanh niên **Tun Tung Tun Sahour** tinh quái). Lợi dụng lúc T-Rex đi ngủ gật, lũ khủng long tí hon này đã lén lút mang những tấm thảm hình chữ nhật/hình vuông đến trải ra để xí chỗ ngủ ké. 

Tấm thảm thứ $i$ được trải cố định từ ô tọa độ trái dưới $(x_{1}, y_{1})$ đến ô tọa độ phải trên $(x_{2}, y_{2})$ (bao gồm cả các ô nằm trên biên của thảm). Vì lũ này cực kỳ láo nháo, các tấm thảm của chúng có thể **đè lên nhau (overlap)** vô tội vạ để tranh giành chỗ mát.

Khi T-Rex tỉnh dậy, nhìn bãi cỏ yêu thích của mình bị thảm của lũ nhóc chiếm đóng, anh chàng liền gầm lên vang dội. T-Rex quyết định sẽ dùng thân hình hộ pháp của mình để giẫm bẹp bất kỳ ô đất nào **còn trống** (chưa bị bất kỳ tấm thảm nào đè lên) nhằm khẳng định chủ quyền làm nơi ngủ trưa. 

Vì cái đầu quá to nhưng hai cánh tay lại quá ngắn không thể cầm bút tính toán, T-Rex ra lệnh cho bạn phải đếm xem **còn lại bao nhiêu ô đơn vị hoàn toàn trống trải** để anh chàng vào việc. Nếu tính sai, bạn sẽ là món tráng miệng thay cho bắp cải!

---

### Đầu vào (Standard Input)
- Dòng đầu tiên chứa ba số nguyên $N, M, K$ ($1 \le N \le 10^5$; $1 \le M, K \le 10^3$).
- $N$ dòng tiếp theo, dòng thứ $i$ chứa 4 số nguyên $x_{1}, y_{1}, x_{2}, y_{2}$ ($1 \le x_{1} \le x_{2} \le M$; $1 \le y_{1} \le y_{2} \le K$) biểu diễn tọa độ thảm của lũ khủng long ăn chực.

---

### Đầu ra (Standard Output)
- In ra một số nguyên duy nhất là số ô đơn vị còn trống để T-Rex dậm chân.

---

### Giới hạn & Subtasks
- **Subtask 1 ($40\%$ số điểm):** $1 \le N \le 1000$; $1 \le M, K \le 100$.
- **Subtask 2 ($60\%$ số điểm):** Không có giới hạn gì thêm ($1 \le N \le 10^5$; $1 \le M, K \le 10^3$).

---

### Ví dụ 1

#### Nhập vào:

```
3 5 5
1 1 3 3
2 2 4 4
5 5 5 5
```

#### In ra:

```
10
```

#### Giải thích ví dụ 1:
> Miếng đất tổng diện tích $5 \times 5 = 25$ ô.
> - Thảm 1 phủ từ $(1,1)$ đến $(3,3)$ $\rightarrow$ Chiếm $9$ ô.
> - Thảm 2 phủ từ $(2,2)$ đến $(4,4)$ $\rightarrow$ Chiếm $9$ ô, nhưng có các ô $(2,2), (2,3), (3,2), (3,3)$ bị trùng với thảm 1.
> - Thảm 3 phủ tại đúng ô $(5,5)$ $\rightarrow$ Chiếm $1$ ô.
>
> Tổng số ô đơn vị bị ít nhất một tấm thảm đè lên là $15$ ô.
> Số ô còn lại hoàn toàn sạch bóng thảm để T-Rex cọc cằn nằm hưởng thụ là: $25 - 15 = 10$ ô.
