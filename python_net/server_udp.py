#!/usr/bin/python3

import socket

data = "welcome to this udp server!!!"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
host = socket.gethostname();
port = 54321;

s.bind((host, port));
print("bind udp on 54321");

while(1):
    recv_data, addr = s.recvfrom(1024);
    print(recv_data.decode(), addr);

s.close();
