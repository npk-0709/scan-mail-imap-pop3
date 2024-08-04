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


def readmail(account: str, limit: int):
    account = account.strip()
    username = account.split('|')[0]
    user = username.split('@')[0]
    password = account.split('|')[1]
    print('[*] ĐANG ĐĂNG NHẬP...')
    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
    mail.login(username, password)
    mail.select("inbox")
    status, messages = mail.search(None, 'UNSEEN')
    mail_ids = messages[0].split()
    print('[*] ĐĂNG NHẬP THÀNH CÔNG, ĐANG SCAN INBOX...')
    count_mail = 0
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
                                    count_mail += 1
                        except:
                            pass
                print(f'{count_mail}|{idbm}|{linkurl}')
                if count_mail >= limit:
                    mail.close()
                    mail.logout()
                    print("* Hoàn Tất .............")
                    return True
    mail.close()
    mail.logout()
    print("* Hoàn Tất .............")
    return True
