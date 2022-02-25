# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:05:25 2021

@author: Administrator
"""

import socket
def main():
    c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        text=input("-->")
        c.sendto(text.encode("utf-8"), ("192.168.70.1",6000))
        if text == "exit":
            break
        ans=c.recvfrom(1024)
        print(ans[0].decode("UTF-8"))   #UDP连接一次断开一次然后重新连接，位置是一样
    c.close()
            
if __name__=="__main__":
    main()