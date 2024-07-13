import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thông tin tài khoản email của bạn
email = "chauaurora9@gmail.com"
password = "qfpcmraezrfiuytc"

# Thông tin người nhận
to_email = "chauaurora9@gmail.com"
subject = "Đây là tiêu đề email"
body = "Đây là nội dung của email. Chúc một ngày tốt lành! 🌞"

# Tạo message object
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to_email
msg['Subject'] = subject

# Thêm nội dung vào email
msg.attach(MIMEText(body, 'plain'))

# Thiết lập máy chủ và gửi email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, to_email, text)
    server.quit()
    print("Email đã được gửi thành công! 🎉")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")