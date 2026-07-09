## Số C

Alice và Bob vào một mùa hè được về quê chơi. Ông bà cho mỗi bạn một máy tính để ôn luyện cho kì thi Tin Học Trẻ vòng khu vực năm nay. Hai bạn rất hào hứng. Vừa được máy tính, Alice liền đố Bob rằng: Ban đầu ở bước $0$, Bob có một danh sách $[0, 0, 0]$. Tại bước thứ $i \space (1 \leq i \leq N)$, Alice yêu cầu Bob cập nhật danh sách ba số $[A_i, B_i, C_i]$ từ ba số $[A_{i - 1}, B_{i - 1}, C_{i - 1}]$ của bước trước theo quy tắc sau:
- $A_i = A_{i-1}+2$
- $B_i = B_{i-1}+A_i$
- $C_i=C_{i-1}+B_i$

Alice muốn biết rằng sau $N$ thì $C_N$ sẽ có giá trị bằng bao nhiêu? Vì số có thể rất lớn nên hãy chia dư cho $10^9+7$.

### Input:
- Một Dòng duy nhất là một số nguyên $N \space (1 \leq N \leq 10^8)$

### Output:
- Một dòng là kết quả duy nhất của bài toán khi chia dư cho $10^9 + 7$

### Scoring

- Subtask 1 ($60\%$ số điểm): $N \leq 10^6$
- Subtask 2 ($20\%$ số điểm): $N \leq 10^7$
- Subtask 3 ($20\%$ số điểm): Không có giới hạn gì thêm

### Ví dụ 1:
#### Nhập vào:
```
1
```
#### In ra:
```
2
```
> #### Giải thích:
> $A_1 = 0 + 2 = 2$
> 
> $B_1 = 0 + 2 = 2$
> 
> $C_1 = 0 + 2 = 2$

### Ví dụ 1:
#### Nhập vào:
```
7
```
#### In ra:
```
168
```
