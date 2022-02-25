# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:32:08 2021

@author: 15003
"""
import socket
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(("",6000))
    while True:
        data,addr=s.recvfrom(1024)
        print("connect by:",addr)
        print("recv data:",data.decode("utf-8"))
        s.sendto(data, addr)
    s.close()
if __name__ == '__main__':
    main()