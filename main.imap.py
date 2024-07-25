import imaplib
import email
import html2text
from email.header import decode_header

data = str(input("Nhập Mail Định Dạng 'Email|Password': ").strip())

# Thông tin đăng nhập
username = data.split('|')[0]
user = username.split('@')[0]
password = data.split('|')[1]
print('[*] ĐANG ĐĂNG NHẬP...')
mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
mail.login(username, password)
mail.select("inbox")
status, messages = mail.search(None, 'UNSEEN')
mail_ids = messages[0].split()
print('[*] ĐĂNG NHẬP THÀNH CÔNG, ĐANG SCAN INBOX...')
for mail_id in mail_ids:
    try:
        status, msg_data = mail.fetch(mail_id, '(RFC822)')
    except:
        continue
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else 'utf-8')
            from_ = msg.get("From")
            idbm = 'None'
            linkurl = 'None'
            if msg.is_multipart():
                for part in msg.walk():
                    try:
                        body = part.get_payload(
                            decode=True).decode('utf-8', 'ignore')
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
mail.close()
mail.logout()
print("* Hoàn Tất .............")
input()
