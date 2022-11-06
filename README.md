
# Project Helper.
**Run project:** 
Chạy các câu lệnh trong cmd thư mục chứa code
```
export FLASK_APP=flasky.py
flask run
```
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