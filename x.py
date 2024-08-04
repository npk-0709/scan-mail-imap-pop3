"""
 * Author: NGUYEN PHU KHUONG (K.AUTO) 
 * Email: dev.phukhuong0709@hotmail.com
 * Github: npk-0709
 * TELE: @khuongdev79
"""

import imaplib
import email
import html2text
from email.header import decode_header
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_email(mail, mail_id, username, user):
    try:
        status, msg_data = mail.fetch(mail_id, '(RFC822)')
        if status != 'OK':
            return None
    except Exception as e:
        print(f"Error fetching mail {mail_id}: {e}")
        return None
    
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
                        body = part.get_payload(decode=True).decode('utf-8', 'ignore')
                        if part.get_content_type() == 'text/html':
                            text = html2text.html2text(body)
                            if user+'+' in body:
                                idbm = body.split(user+'+')[1].split('@')[0].split('-')[1]
                                linkurl = "https://fb.me/" + body.split("fb.me/")[1].split('"')[0]
                                with open(f'{username}.result.txt', 'a+', encoding='utf-8') as f:
                                    f.write(f'{idbm}|{linkurl}\n')
                    except Exception as e:
                        print(f"Error processing part: {e}")
                        continue
            return f'{idbm}|{linkurl}'
    return None

def main():
    data = str(input("Nhập Mail Định Dạng 'Email|Password: '").strip())
    username = data.split('|')[0]
    user = username.split('@')[0]
    password = data.split('|')[1]

    print('[*] ĐANG ĐĂNG NHẬP...')
    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
    mail.login(username, password)
    mail.select("inbox")
    status, messages = mail.search(None, 'ALL')
    mail_ids = messages[0].split()
    print('[*] ĐĂNG NHẬP THÀNH CÔNG, ĐANG SCAN INBOX...')

    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(fetch_email, mail, mail_id, username, user): mail_id for mail_id in mail_ids}
        for future in as_completed(futures):
            result = future.result()
            if result:
                print(result)
    
    mail.close()
    mail.logout()
    print("* Hoàn Tất .............")
    input()

if __name__ == "__main__":
    main()
