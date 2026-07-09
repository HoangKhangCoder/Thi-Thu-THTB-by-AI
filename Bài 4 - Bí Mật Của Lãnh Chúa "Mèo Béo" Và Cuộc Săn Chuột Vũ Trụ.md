# Bí Mật Của Lãnh Chúa "Mèo Béo" Và Cuộc Săn Chuột Vũ Trụ

Năm $2026$, tại hành tinh Cát-Nip, Lãnh chúa **Mèo Béo** nổi tiếng là vị vua lười biếng nhất dải ngân hà nhưng lại sở hữu một kho báu chứa đầy "Cỏ Mèo Vũ Trụ". Thảm họa ập đến khi một đàn chuột không gian đổ bộ và tấn công vào hệ thống $N$ kho lương thực của ông.

Hệ thống kho lương thực được thiết kế theo dạng một **Đồ thị có hướng dạng đường thẳng** gồm $N$ kho được đánh số từ $1$ đến $N$. Kho $i$ chứa $A_i$ túi Cỏ Mèo và chỉ có một đường đi một chiều duy nhất từ kho $i$ sang kho $i + 1$ ($1 \le i < N$).

Lãnh chúa Mèo Béo quá mập để di chuyển xa, nhưng ông sở hữu một chiếc máy hút tự động có tầm hoạt động (chiều dài) đúng $K$ kho liên tiếp. Máy hút này có thể đặt tại bất kỳ kho $i$ nào và sẽ thu gom toàn bộ Cỏ Mèo từ kho $i$ đến kho $i + K - 1$.

Tuy nhiên, lũ chuột rất gian xảo: Mỗi khi Mèo Béo bật máy hút tại một đoạn $K$ kho, lũ chuột sẽ ngay lập tức cướp sạch Cỏ Mèo ở các kho nằm **ngay trước** và **ngay sau** đoạn hút đó (tức là kho $i - 1$ và kho $i + K$, nếu các kho này tồn tại).

Vì quá lười suy nghĩ, Lãnh chúa Mèo Béo hứa sẽ thưởng cho bạn một đĩa cá hồi siêu bự nếu bạn giúp ông chọn vị trí đặt máy hút (chính xác $K$ kho liên tiếp) sao cho **Lợi Nhuận Thu Được** là lớn nhất. 

$$\text{Lợi Nhuận} = (\text{Tổng Cỏ Mèo hút được}) - (\text{Tổng Cỏ Mèo bị chuột cướp})$$

Bạn hãy viết chương trình tìm Lợi Nhuận lớn nhất mà Lãnh chúa Mèo Béo có thể đạt được!

---

### Đầu vào (Standard Input)
- Dòng đầu tiên chứa hai số nguyên $N$ và $K$ ($1 \le K \le N \le 10^6$).
- Dòng thứ hai chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$) biểu diễn số túi Cỏ Mèo tại từng kho.

---

### Đầu ra (Standard Output)
- In ra một số nguyên duy nhất là Lợi Nhuận lớn nhất tìm được.

---

### Giới hạn & Subtasks
- **Subtask 1 ($30\%$ số điểm):** $1 \le K \le N \le 1000$.
- **Subtask 2 ($70\%$ số điểm):** $1 \le K \le N \le 10^6$.

---

### Ví dụ 1

#### Nhập vào:
```
6 3
2 1 5 3 4 1
```

### In ra
```
10
```

### Giải thích ví dụ 1:
>Xét tất cả các vị trí đặt máy hút có độ dài $K = 3$ trên dãy $A = [2, 1, 5, 3, 4, 1]$:
>
>1. Đặt máy hút tại kho $1$ đến kho $3$ (các kho $1, 2, 3$):
>   - Hút được: $2 + 1 + 5 = 8$.
>   - Bị chuột cướp: kho $4$ (giá trị $3$).
>   - Lợi nhuận $= 8 - 3 = 5$.
>
>2. Đặt máy hút tại kho $2$ đến kho $4$ (các kho $2, 3, 4$):
>   - Hút được: $1 + 5 + 3 = 9$.
>   - Bị chuột cướp: kho $1$ (giá trị $2$) và kho $5$ (giá trị $4$).
>   - Lợi nhuận $= 9 - (2 + 4) = 3$.
>
>3. Đặt máy hút tại kho $3$ đến kho $5$ (các kho $3, 4, 5$):
>   - Hút được: $5 + 3 + 4 = 12$.
>   - Bị chuột cướp: kho $2$ (giá trị $1$) và kho $6$ (giá trị $1$).
>   - Lợi nhuận $= 12 - (1 + 1) = 10$.
>
>4. Đặt máy hút tại kho $4$ đến kho $6$ (các kho $4, 5, 6$):
>   - Hút được: $3 + 4 + 1 = 8$.
>   - Bị chuột cướp: kho $3$ (giá trị $5$).
>   - Lợi nhuận $= 8 - 5 = 3$.
>
>Kết quả lợi nhuận lớn nhất tìm được là $10$ (khi chọn đặt máy hút từ kho $3$ đến kho $5$).
