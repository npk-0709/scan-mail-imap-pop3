import poplib
import email
import html2text
from email.header import decode_header

data = str(input("Nhập Mail Định Dạng 'Email|Password': ").strip())

# Thông tin đăng nhập
username = data.split('|')[0]
user = username.split('@')[0]
password = data.split('|')[1]
print('[*] ĐANG ĐĂNG NHẬP...')

# Kết nối tới máy chủ POP3
mail = poplib.POP3_SSL('pop-mail.outlook.com')
mail.user(username)
mail.pass_(password)
print('[*] ĐĂNG NHẬP THÀNH CÔNG, ĐANG SCAN INBOX...')

# Lấy số lượng email
num_messages = len(mail.list()[1])

for i in range(num_messages):
    try:
        response, lines, octets = mail.retr(i + 1)
    except:
        continue

    # Ghép nối các dòng để tạo thành nội dung email hoàn chỉnh
    msg_data = b'\r\n'.join(lines)
    msg = email.message_from_bytes(msg_data)

    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else 'utf-8')
    from_ = msg.get("From")
    idbm = 'None'
    linkurl = 'None'
    if msg.is_multipart():
        for part in msg.walk():
            try:
                body = part.get_payload(decode=True).decode('utf-8', 'ignore')
                if part.get_content_type() == 'text/html':
                    text = html2text.html2text(body)
                    if user+'+' in body:
                        idbm = body.split(
                            user+'+')[1].split('@')[0].split('-')[1]
                        linkurl = "https://fb.me/" + \
                            body.split("fb.me/")[1].split('"')[0]
                        with open(f'{username}.result.txt', 'a+', encoding='utf-8') as f:
                            f.write(f'{idbm}|{linkurl}\n')
            except:
                pass
    print(f'{idbm}|{linkurl}')

mail.quit()
print("* Hoàn Tất .............")
input()
