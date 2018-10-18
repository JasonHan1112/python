#!/usr/bin/python3

import socket

data = "this is me!!!"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

host = socket.gethostname();
port = 54321;

s.sendto(data.encode(), (host, port));


