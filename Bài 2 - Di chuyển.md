## Di chuyển

Trong kỳ nghỉ hè tại quê, Alice và Bob cùng nhau sáng tạo một trò chơi trên lưới tọa độ vuông $N \times M$. Các hàng được đánh số từ $1$ đến $N$ từ trên xuống dưới, các cột được đánh số từ $1$ đến $M$ từ trái sang phải. 

Ô ở hàng $i$, cột $j$ được ký hiệu là ô $(i, j)$ và chứa một giá trị điểm $A_{i, j}$. Một người chơi bắt đầu từ ô $(1, 1)$ và cần di chuyển đến ô $(N, M)$. Từ ô $(i, j)$, người chơi chỉ có thể **di chuyển sang ô bên phải $(i, j+1)$** hoặc **xuất phát xuống ô bên dưới $(i+1, j)$**.

Bob đưa ra một thử thách cho Alice: Trong quá trình di chuyển từ $(1, 1)$ đến $(N, M)$, Alice phải nhặt các giá trị $A_{i, j}$ trên đường đi. Tổng điểm thu được là **tích** của tất cả các ô trên hành trình đó. Alice muốn chọn một hành trình sao cho tích các số trên đường đi có **số lượng chữ số $0$ tận cùng là nhiều nhất có thể**.

Hãy giúp Alice tìm ra số lượng chữ số $0$ tận cùng lớn nhất đó!

### Input:
- Dòng đầu tiên chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên không âm $A_{i, j}$ ($0 \le A_{i, j} \le 10^9$) mô tả bảng điểm.

### Output:
- Một dòng duy nhất chứa một số nguyên là số lượng chữ số $0$ tận cùng nhiều nhất của tích các số trên đường đi từ $(1, 1)$ đến $(N, M)$.

### Scoring
- Subtask 1 ($30\%$ số điểm): $N, M \le 10$.
- Subtask 2 ($40\%$ số điểm): $N, M \le 500$ và $A_{i, j} > 0$.
- Subtask 3 ($30\%$ số điểm): $N, M \le 1000$ và $A_{i, j} \ge 0$.

---

### Ví dụ 1:
#### Nhập vào:
```
3 3
2 5 1
4 10 2
1 2 5
```

#### In ra:
```
3
```

> #### Giải thích:
> Đường đi tối ưu là: (1,1) -> (1,2) -> (2,2) -> (2,3) -> (3,3).  
> Các giá trị tương ứng: 2 x 5 x 10 x 2 x 5 = 1000.  
> Số 1000 có 3 chữ số 0 tận cùng.

---

### Ví dụ 2:
#### Nhập vào:
```
2 2
2 5
5 2
```
#### In ra:
```
1
```
> #### Giải thích:
> - Đường đi 1: $(1,1) \rightarrow (1,2) \rightarrow (2,2)$ có tích là $2 \times 5 \times 2 = 20$ ($1$ chữ số $0$).
> - Đường đi 2: $(1,1) \rightarrow (2,1) \rightarrow (2,2)$ có tích là $2 \times 5 \times 2 = 20$ ($1$ chữ số $0$).
> Kết quả là $1$.
