# Kỷ Lục Đỉnh Cao Của T-Rex Trong "Súp Quay Súp Phở"

Tại thung lũng Gomora năm $2026$, cơn sốt game di động **Súp Quay Súp Phở** (một trò chơi chạy vô tận né chướng ngại vật siêu kinh điển) đang khiến toàn bộ cư dân khủng long điên đảo. Đại ca **T-Rex Cọc Cằn** tuy tay ngắn nhưng lại là một game thủ hệ "try-hard" chính hiệu, sở hữu chiếc điện thoại màn hình $3D$ độ phân giải không gian siêu thực.

Trong bản cập nhật mới nhất, trò chơi mở ra một đấu trường không gian $3D$ dạng khối hộp có kích thước $X \times Y \times Z$ ô đơn vị. Hệ tọa độ của đấu trường có góc trái-dưới-gần là $(1, 1, 1)$ và góc phải-trên-xa là $(X, Y, Z)$. 

Thanh niên **Tun Tung Tun Sahour** vì ghen tị với điểm số kỷ lục của T-Rex nên đã lén hack vào hệ thống game, thả vào đấu trường $N$ khối chướng ngại vật nhiễm độc hình hộp chữ nhật hoặc hình lập phương. Khối chướng ngại vật thứ $i$ chiếm trọn không gian từ tọa độ $(x_{1}, y_{1}, z_{1})$ đến $(x_{2}, y_{2}, z_{2})$ (bao gồm cả các ô đơn vị nằm trên biên và bề mặt của khối). Các khối chướng ngại vật này cực kỳ dị hợm, chúng có thể **đè lên nhau (overlap)** ở các vùng không gian bị trùng lặp.

Nhiệm vụ của nhân vật do T-Rex điều khiển là phải lách qua các khe hở để thu thập các vật phẩm đặc biệt. Tuy nhiên, các vật phẩm này chỉ xuất hiện tại những **ô đơn vị hoàn toàn an toàn** — tức là những ô $3D$ trống trải, chưa bị bất kỳ một khối chướng ngại vật nào của Tun Tung Tun Sahour đè lên.

T-Rex cần biết chính xác **còn lại bao nhiêu ô đơn vị $3D$ an toàn** trong toàn bộ đấu trường $X \times Y \times Z$ để lên chiến thuật "phá đảo" trò chơi. Đôi tay ngắn ngủn của anh chàng không thể vuốt màn hình để đếm hết không gian $3D$ phức tạp này được. Bạn hãy lập trình giải cứu kỷ lục thế giới của T-Rex trước khi anh chàng cọc cằn này đập nát cái điện thoại!

---

### Đầu vào (Standard Input)
- Dòng đầu tiên chứa bốn số nguyên $N, X, Y, Z$ ($1 \le N \le 10^5$; $1 \le X, Y, Z \le 200$).
- $N$ dòng tiếp theo, dòng thứ $i$ chứa 6 số nguyên biểu diễn tọa độ khối chướng ngại vật: $x_{1}, y_{1}, z_{1}, x_{2}, y_{2}, z_{2}$ ($1 \le x_{1} \le x_{2} \le X$; $1 \le y_{1} \le y_{2} \le Y$; $1 \le z_{1} \le z_{2} \le Z$).

---

### Đầu ra (Standard Output)
- In ra một số nguyên duy nhất là số ô đơn vị $3D$ hoàn toàn an toàn còn lại trong game.

---

### Giới hạn & Subtasks
- **Subtask 1 ($30\%$ số điểm):** $1 \le N \le 100$; $1 \le X, Y, Z \le 30$.
- **Subtask 2 ($40\%$ số điểm):** $1 \le N \le 1000$; $1 \le X, Y, Z \le 100$.
- **Subtask 3 ($30\%$ số điểm):** Không có giới hạn gì thêm ($1 \le N \le 10^5$; $1 \le X, Y, Z \le 200$).

---

### Ví dụ 1

#### Nhập vào:

```
2 3 3 3
1 1 1 2 2 2
2 2 2 3 3 3
```

#### In ra:

```
13
```

#### Giải thích ví dụ 1:
> Đấu trường $3D$ có tổng thể tích là $3 \times 3 \times 3 = 27$ ô đơn vị.
> - Khối chướng ngại vật 1 phủ từ $(1,1,1)$ đến $(2,2,2)$ $\rightarrow$ Chiếm $2 \times 2 \times 2 = 8$ ô.
> - Khối chướng ngại vật 2 phủ từ $(2,2,2)$ đến $(3,3,3)$ $\rightarrow$ Chiếm $2 \times 2 \times 2 = 8$ ô.
> - Hai khối này giao nhau (overlap) duy nhất tại chính ô đơn vị tọa độ $(2,2,2)$.
>
> Tổng số ô đơn vị bị nhiễm độc bởi chướng ngại vật là: $8 + 8 - 1 = 15$ ô.
> Số ô $3D$ hoàn toàn an toàn còn sót lại cho T-Rex ăn vật phẩm là: $27 - 15 = 13$ ô.
