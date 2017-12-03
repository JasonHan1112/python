import os;
import requests;
from bs4 import BeautifulSoup

class c_spider_test():
    

    def __init__(self,url):
        self.url = url;
        print("spider on: "+ self.url);
    
    def request_url(self):
        self.request_get = requests.get(self.url);
        self.request_status = self.request_get.status_code;
        print("request_status = ", self.request_status);
        #print("text\r\n", self.request_get.text);
        #print("content:\r\n", );
        #print(self.request_get.content);
        print("type(self.request_get) = ", type(self.request_get));
        print("headers");
        print(self.request_get.headers);
        print("encoding");
        print(self.request_get.encoding);
        print("cookies");
        print(self.request_get.cookies);
    
    def file_open(self, path, o_mode):
        self.file = open(path, mode=o_mode);
            
    def file_read(self, path):
        self.file_open(path, "r");
        print(self.file.read());
    
    def file_write(self, path, content):
        self.file_open(path, "wb");#need open with binary, browser can parse
        self.file.write(content);


