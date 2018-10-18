#!/usr/bin/python3

import socket
data = "welcome to this server!!!";
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
host = socket.gethostname();
port = 12345;
s.bind((host, port));

s.listen(5)
while(1):
    print("waiting for connect...");
    client, addr = s.accept();
    print("connected:addr = ", addr);
    client.sendall(data.encode());
    client.close();
