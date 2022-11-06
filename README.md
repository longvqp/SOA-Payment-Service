
# Project Helper.
**Run project:** 
Tại thư mục chứa sources code 
```
py -3 -m venv .venv
```

sau đó khởi chạy venv
```
.venv\Scripts\activate
```

Update pip in the virtual environment
```
python -m pip install --upgrade pip
```

cài đặt các thư viện cần thiết
```
pip install –r requirements.txt
```

Khởi chạy hệ thống
```
set FLASK_APP=flasky.py
set FLASK_DEBUG=1
```
Chạy server
```
flask run
```
truy cập website với đường link: 127.0.0.1:5000

**Sử dụng hệ thống:**
- Sau khi khởi chạy flask run, hệ thống sẽ chạy trên localhost.
- Có thể dùng chức năng đăng ký Register trên thanh navbar để thêm sinh viên mới với mục đích kiểm tra hệ thống
- Dùng chức năng đăng nhập Login trên thanh navbar để đăng nhập vào sử dụng hệ thống
- Sau khi đăng nhập thành công hệ thống sẽ dẫn đến trang thanh toán học phí
- Nhập mã số sinh viên với học phí cần thanh toán vào mục Student ID Indept
- Hệ thống sẽ hiển thị thông tin của sinh viên đang nợ học phí.
- Click chọn agree all term để xác nhận điều khoản hệ thống (mô phỏng)
- Click Pay để tiến hành thanh toán.
- Hệ thống gửi OTP về qua mail của sinh viên thanh toán, mã OTP có thời hạn 5 phút
- Sau khi nhập vào chính xác mã OTP hệ thống sẽ thông báo thanh toán thành công qua email cho cả người nhận và người gửi.

**Nạp tiền vào Tài Khoản: (Mô phỏng)**
- Sau khi đăng nhập thành công sinh viên có thể vào trang Information để kiểm tra thông tin và nạp tiền vào tài khoản
- Click vào mục Update Balance, một form sẽ hiện ra và sinh viên nhập số tiền cần nạp vào tài khoản nhằm mục đích thanh toán học phí.

**Các tài khoản được cung cấp:**
-Tài khoản sinh viên
```
Mã số sinh viên: 51800899
Password: 123123
Nợ học phí: 8000000.
Số dư: 0
```
```
Mã số sinh viên: 51900900
Password: 123123
Nợ học phí: 9000000.
Số dư: 1000
```
```
Mã số sinh viên: 51900901
Password: 123123
Nợ học phí: 7000000.
Số dư: 9999999
```


