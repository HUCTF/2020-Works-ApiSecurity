from .NIC_package_get import NICRUN
from threading import Thread
from .scanapi import RQRUN
import os

def RUNThread(website, choice):
    thread = Thread(target=NICRUN, args=[netname, needpcap, str(current_user.username)])
    # 使用多线程
    thread.start()
    thread = Thread(target=RQRUN)
    # 使用多线程
    thread.start()
    
    thread = Thread(target=send_async_email, args=[app, message])
    thread.start()

WEBSITE=os.environ.get('WEBSITE')
USERNAME=os.environ.get('USERNAME')
PASSWD=os.environ.get('PASSWD')
COOKIE=os.environ.get('COOKIE')

