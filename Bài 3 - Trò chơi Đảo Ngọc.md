## Trò chơi Đảo Ngọc

Trong một vùng biển thuộc quần đảo Trường Sa, có $N$ hòn đảo nhỏ được mô hình hóa thành các điểm trên mặt phẳng tọa độ $Oxy$. Hòn đảo thứ $i$ nằm tại tọa độ $(X_i, Y_i)$ và chứa một lượng đá quý có giá trị là $V_i$. Không có hai hòn đảo nào nằm cùng tọa độ.

Alice và Bob cùng tham gia một trò chơi thu thập đá quý trên biển. Ban đầu, tàu của hai bạn đang neo đậu tại gốc tọa độ $(0, 0)$. Hai bạn thay phiên nhau di chuyển tàu (Alice đi trước). Quy tắc di chuyển như sau:
1. Từ vị trí hiện tại $(x, y)$, người chơi có thể di chuyển tàu đến bất kỳ hòn đảo $i$ chưa từng được ghé thăm sao cho đảo đó nằm ở **phía trên và bên phải** vị trí hiện tại (nghĩa là $X_i \ge x$ và $Y_i \ge y$, đồng thời không trùng vị trí hiện tại).
2. Khi di chuyển đến hòn đảo $i$, người chơi sẽ thu thập toàn bộ $V_i$ đá quý trên đảo đó vào kho chung của cả hai.
3. Trò chơi kết thúc khi đến lượt một người chơi nhưng **không thể di chuyển** đến bất kỳ hòn đảo nào hợp lệ nữa.

Để tăng tính hấp dẫn, Bob đặt ra một điều kiện bổ sung: Trò chơi chỉ được coi là **"Thành công"** nếu tổng giá trị đá quý thu thập được trên cả hành trình là một **số lẻ** và **số lượng hòn đảo được ghé thăm đúng bằng $K$**.

### Yêu cầu:
1. Tính số lượng đường đi khác nhau gồm đúng $K$ hòn đảo sao cho tổng giá trị đá quý là số lẻ. Vì số đường đi có thể rất lớn, hãy in ra kết quả sau khi chia dư cho $10^9 + 7$.
2. Tìm tổng giá trị đá quý lớn nhất có thể thu được trong tất cả các đường đi hợp lệ gồm $K$ hòn đảo (không bắt buộc tổng phải lẻ). Nếu không có đường đi nào độ dài $K$, in ra $-1$.

### Input:
- Dòng thứ nhất chứa hai số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- $N$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên $X_i, Y_i, V_i$ ($0 \le X_i, Y_i \le 10^9$, $1 \le V_i \le 10^9$) lần lượt là tọa độ và giá trị đá quý của hòn đảo thứ $i$.

### Output:
- Dòng thứ nhất: Số lượng đường đi thỏa mãn điều kiện "Thành công" (chia dư cho $10^9 + 7$).
- Dòng thứ hai: Tổng giá trị đá quý lớn nhất thu được từ một đường đi độ dài $K$. Nếu không tồn tại đường đi độ dài $K$, in ra $-1$.

### Scoring:
- Subtask 1 ($20\%$  số điểm): $N \le 10, K \le N$.
- Subtask 2 ($30\%$  số điểm): $N \le 1000, K \le N$.
- Subtask 3 ($30\%$  số điểm): $N \le 10^5, K \le 20$.
- Subtask 4 ($20\%$  số điểm): Không có giới hạn gì thêm.

---

### Ví dụ 1:
#### Nhập vào:
```
4 2
1 2 3
2 4 4
3 1 5
4 5 2
```
#### In ra:
```
2
9
```
> #### Giải thích:
> Các đường đi độ dài $K=2$ bắt đầu từ $(0,0)$:
> - $(0,0) \rightarrow (1,2) \rightarrow (2,4)$: Tổng giá trị = $3 + 4 = 7$ (Lẻ) $\rightarrow$ Thỏa mãn.
> - $(0,0) \rightarrow (1,2) \rightarrow (4,5)$: Tổng giá trị = $3 + 2 = 5$ (Lẻ) $\rightarrow$ Thỏa mãn.
> - $(0,0) \rightarrow (3,1) \rightarrow (4,5)$: Tổng giá trị = $5 + 2 = 7$ (Lẻ) $\rightarrow$ Thỏa mãn.
> - $(0,0) \rightarrow (2,4) \rightarrow (4,5)$: Tổng giá trị = $4 + 2 = 6$ (Chẵn).
> 
> Số đường đi có tổng lẻ là $3$ (Lưu ý ví dụ minh họa kiểm tra điều kiện).
> Giá trị lớn nhất thu được từ đường đi độ dài $2$ là $3 + 6 = 9$ (từ $(1,2) \rightarrow (2,4)$ hoặc $(3,1) \rightarrow (4,5)$ tùy chọn kết hợp).

---

### Ví dụ 2:
#### Nhập vào:
```
3 3
1 1 2
2 2 4
3 3 6
```
#### In ra:
```
0
12
```
> #### Giải thích:
> Chỉ có $1$ đường đi duy nhất độ dài $3$: $(1,1) \rightarrow (2,2) \rightarrow (3,3)$ với tổng giá trị $2 + 4 + 6 = 12$ (Chẵn).
> Do đó số đường đi có tổng lẻ là $0$. Giá trị lớn nhất thu được là $12$.
