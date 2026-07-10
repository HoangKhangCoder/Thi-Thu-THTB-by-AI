# Chấn Động World Cup 2026: Tin Đồn Trọng Tài Thiên Vị Cầu Thủ "Biển Dơ"

Mùa hè năm $2026$, bầu không khí World Cup đang nóng hơn bao giờ hết. Tuy nhiên, một đại thảm họa truyền thông đã nổ ra trên mạng xã hội từ một tài khoản ẩn danh mang tên **"Tun Tung Tun Sahour"**. Tài khoản này khẳng định vị trọng tài chính đã nhận hối lộ để thiên vị trắng trợn cho **Biển Dơ** — siêu sao tiền đạo khét tiếng với lối đá "lươn lẹo", chuyên có những pha té ngã ăn vạ đậm chất điện ảnh trong vòng cấm để kiếm quả phạt đền, giúp anh ta dễ dàng ôm cúp.

Để chứng minh điều này, Tun Tung Tun Sahour đã tung lên mạng đúng $N$ tệp tài liệu mật (vốn là các file ghi âm tiếng cười đầy âm mưu của trọng tài và Biển Dơ). Luồng thông tin chấn động này đã bay thẳng tới tai của **T-Rex Ngố** — một con khủng long bạo chúa ăn chay, siêu cấp lười biếng nhưng lại cực kỳ thích hóng biến.

T-Rex Ngố quyết định phải tải ngay $N$ tệp tài liệu này về và chia nhỏ chúng thành các nhóm bảo mật để đem đi giấu trong các hang động nhằm tránh bị thế lực ngầm của siêu sao Biển Dơ xóa sổ. 

Tuy nhiên, vì đầu óc của T-Rex rất ngố và đôi tay thì quá ngắn, nó quy định việc chia nhóm phải tuân theo các luật kỳ quặc sau:
1. Mỗi nhóm hang động phải chứa ít nhất $1$ tệp tài liệu.
2. Tổng số lượng tệp tài liệu trong tất cả các nhóm phải bằng chính xác $N$.
3. Các hang động hoàn toàn giống hệt nhau, do đó thứ tự của các nhóm không quan trọng. Ví dụ, việc chia tệp tài liệu thành các nhóm có số lượng là $(1, 2)$ và $(2, 1)$ chỉ được tính là $1$ cách duy nhất!

Tun Tung Tun Sahour hứa sẽ tặng cho T-Rex Ngố một xe tải chứa đầy lá cây bắp cải nếu nó tính được có bao nhiêu cách chia nhóm thỏa mãn. T-Rex Ngố bó tay vì tay quá ngắn không đếm ngón được, bạn hãy giải cứu nó! Vì kết quả có thể cực kỳ khổng lồ, hãy chia lấy dư cho $10^9 + 7$.

---

### Đầu vào (Standard Input)
- Dòng duy nhất chứa một số nguyên $N$ biểu diễn tổng số tệp tài liệu mật về cầu thủ Biển Dơ ($1 \le N \le 10^5$).

---

### Đầu ra (Standard Output)
- In ra một số nguyên duy nhất là số cách chia nhóm tài liệu bảo mật sau khi chia dư cho $10^9 + 7$.

---

### Giới hạn & Subtasks
- **Subtask 1 ($30\%$ số điểm):** $1 \le N \le 100$.
- **Subtask 2 ($40\%$ số điểm):** $1 \le N \le 1000$.
- **Subtask 3 ($30\%$ số điểm):** $1 \le N \le 5 \times 10^4$.

---

### Ví dụ 1

#### Nhập vào:

```
3
```

#### In ra:
```
3
```

#### Giải thích ví dụ 1:
> Với $N = 3$ tệp tài liệu mật, T-Rex Ngố có đúng $3$ cách chia vào các hang động (do không tính thứ tự):
> - Cách 1: Gộp chung cả $3$ tệp vào $1$ hang: $[3]$
> - Cách 2: Chia thành hai hang, một hang $2$ tệp, một hang $1$ tệp: $[2, 1]$ (nhóm $[1, 2]$ tính trùng là cách này).
> - Cách 3: Chia đều mỗi hang $1$ tệp: $[1, 1, 1]$
