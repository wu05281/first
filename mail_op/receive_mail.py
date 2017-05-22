#coding=utf-8
import imapclient, sys, pyzmail

imap_obj = imapclient.IMAPClient(host='imap.qq.com')
try:
    imap_obj.login('37809131@qq.com', '************')
except imap_obj.Error:
    print('Could not log in')
    sys.exit(1)
else:
    imap_obj.select_folder('INBOX', readonly=True)
    UIDs = imap_obj.search(['UNSEEN'])
    for UID in UIDs:
        rawMessages = imap_obj.fetch([UID], [b'BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
        print(message.get_addresses('from'))
        print(message.get_addresses('to'))
        print(message.get_addresses('cc'))
        if message.text_part:
            print(message.text_part.get_payload().decode(message.text_part.charset))
        if message.html_part:
            print(message.html_part.get_payload().decode(message.html_part.charset))
        print(message.get_subject())
        print('#'*30)
finally:
    imap_obj.logout()
