#lib

import urllib.request


#function
#################################
def hello_web():
    '''
    down_data = urllib.request.urlopen("http://www.baidu.com");
    print("##geturl:\n", down_data.geturl());
    print("##down file info:\n", down_data.info());
    print("##code:\n", down_data.getcode());
    data = down_data.readlines();#list
    print(data[500]);
    '''
    #another way to realize 
    
    #build opener
    opener = urllib.request.build_opener();
    down_data = opener.open("http://www.baidu.com");
    print("##geturl:\n", down_data.geturl());
    print("##down file info:\n", down_data.info());
    print("##code:\n", down_data.getcode());



def down_file():
    download_file = urllib.request.urlretrieve("http://blog.csdn.net/weiwei_pig/article/details/51178226", filename = "./baidu.html");#save page
    urllib.request.urlcleanup();#clean cache
    
def quote_test():
    qoute_str = urllib.request.quote("http://www.baidu.com");
    print(qoute_str);
    unqoute_str = urllib.request.unquote(qoute_str);
    print(unqoute_str);

def change_header(url = "http://blog.csdn.net/", file_name = "./change_header_response.html"):
    headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0");
    opener = urllib.request.build_opener();
    opener.addheaders = [headers];
    data = opener.open(url).read();
    fhandle = open(file_name, "wb");
    fhandle.write(data);
    fhandle.close();

def get_method():
    key_word = "韩雪晴";
    #url = "https://www.baidu.com/s?wd=%E9%9F%A9%E9%9B%AA%E6%99%B4";
    key_word_quoted = urllib.request.quote(key_word);
    print("key_word_quoted", key_word_quoted);
    url = "https://www.baidu.com/s?wd=";
    url_key_word_qouted = url+key_word_quoted;
    change_header(url_key_word_qouted, "xueqing_baidu.html");

def post_method():
    url = "http://www.iqianyue.com/mypost";
    #construct post info
    post_data = urllib.parse.urlencode({"name":"xueqing", "pass":"123456"}).encode("utf-8");
   
    #construct post request
    #req = urllib.request.Request(url, post_data);
    req = urllib.request.Request(url, post_data, method = "POST");
    #construct header for request
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; \
    rv:57.0) Gecko/20100101 Firefox/57.0");
    
    #request post data and get response
    data_response = urllib.request.urlopen(req).read();
    
    #save file
    fhandle = open("post_test.html", "wb");
    fhandle.write(data_response);
    fhandle.close();

def use_proxy(proxy_addr, url):
    proxy = urllib.request.ProxyHandler({"http":proxy_addr});
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler);

    '''
    urllib.request.install_opener(opener);
    data = urllib.request.urlopen(url).read().decode("utf-8");
    '''
    #equal to up
    data = opener.open(url).read().decode("utf-8");
    return data;

def debug_log_test():
    httphd = urllib.request.HTTPHandler(debuglevel = 1);
    httpshd = urllib.request.HTTPSHandler(debuglevel = 1);
    opener = urllib.request.build_opener(httphd, httpshd);
    data = opener.open("http://edu.51cto.com");

def url_exception():
    try:
        urllib.request.urlopen("http://blog.csdn333333.net");
    except urllib.error.URLError as e:
        print(e.reason);
    except urllib.error.HTTPError as e:
        print(e.code);
        print(e.reason);

def log_in_without_cookies(url1 = "", url2 = ""):
    if url1 == "" or url2 =="":
        print("need a url");
        return;

    #urlencode and ntf-8 encode
    post_data = urllib.parse.urlencode({
        "username":"weisuen",
        "password":"aA123456"
    }).encode("utf-8");
    
    #construct post request
    req = urllib.request.Request(url1, post_data);
    #construct header for request
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; \
    Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0");

    #open url and read content
    data = urllib.request.urlopen(req).read();
    
    #write files
    fhandle = open("log_in_without_cookies1.html", "wb");
    fhandle.write(data);
    fhandle.close();

    #construct post request
    req = urllib.request.Request(url2);
    #construct header for request
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; \
    Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0");

    #open url and read content
    data = urllib.request.urlopen(req).read();
    
    #write files
    fhandle = open("log_in_without_cookies2.html", "wb");
    fhandle.write(data);

    fhandle.close();
    return;


import http.cookiejar
def log_in_with_cookies(url1 = "", url2 = ""):
    if url1 == "" or url2 =="":
        print("need a url");
        return;

    #urlencode and ntf-8 encode
    post_data = urllib.parse.urlencode({
        "username":"weisuen",
        "password":"aA123456"
    }).encode("utf-8");

    #construct post request
    req = urllib.request.Request(url1, post_data);
    #construct header for request
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; \
    Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0");

    #use cookiejar
    cjar = http.cookiejar.CookieJar();

    #construct opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar));

    #install opener, global opener, after this urlopen() will use this opener
    urllib.request.install_opener(opener);

    data_save = opener.open(req).read();
    
    #write files
    fhandle = open("log_in_with_cookies1.html", "wb");
    fhandle.write(data_save);
    fhandle.close();

    #construct post request
    req = urllib.request.Request(url2);
    #construct header for request
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; \
    Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0");

    #open url and read content
    data = urllib.request.urlopen(req).read();
    
    #write files
    fhandle = open("log_in_with_cookies2.html", "wb");
    fhandle.write(data);

    fhandle.close();



import re;
def spider_actual_combat(url, page):
    if url == "":
        print("need a url");
        return;
    headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0");
    opener = urllib.request.build_opener();
    opener.addheaders = [headers];
    html1 = opener.open(url).read();
    
    pattern1 = '<img width="200" height="200" class="err-product" data-img="1" src="//(.+?\.jpg)';
    html1 = str(html1);
    result1 = re.compile(pattern1).findall(html1);
    #print(result1);
    i = 0;
    for image in result1:
        image_name = "./jd_download_jpg/jd_linux"+str(page)+"_"+str(i)+".jpg";
        image_url = "http://"+image;
        print(image_url);
        try:
            urllib.request.urlretrieve(image_url, filename=image_name);
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                i += 1;
            if hasattr(e, "reason"):
                i += 1;
        i += 1;
    
    



#demo
#################################
#hello_web();

'''
for i in range(0,10):
    print(str(i));
    down_file();
'''

#quote_test();

'''
for i in range(0, 10):
    print(str(i));
    change_header();
'''

#get_method();

#post_method();

'''
proxy_addr = "223.96.95.229:3128";
data = use_proxy(proxy_addr, "http://www.baidu.com");
print(len(data));
'''

#debug_log_test();

#url_exception();

#without cookies
'''
url1_login_without_cookies = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LtxBx";
url2_login_without_cookies = "http://bbs.chinaunix.net/"

#url2_login_without_cookies.html still display need login
log_in_without_cookies(url1_login_without_cookies, url2_login_without_cookies);
'''

'''
#with cookies
url1_login_with_cookies = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LtxBx";
url2_login_with_cookies = "http://bbs.chinaunix.net/"

#url2_login_with_cookies.html still display need login
log_in_with_cookies(url1_login_with_cookies, url2_login_with_cookies);
'''
for i in range(1, 50):
    url = 'https://search.jd.com/Search?keyword=linux&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=linux&page='+str(i);
    spider_actual_combat(url, i);


