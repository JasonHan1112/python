from c_spider_test import c_spider_test

#get content
url = "https://www.baidu.com/";
object_spider = c_spider_test(url);
object_spider.request_url();
object_spider.file_write("./request.content", object_spider.request_get.content);

#get image
# //www.baidu.com/img/bd_logo1.png
url = "https://www.baidu.com/img/bd_logo1.png";
object_spider = c_spider_test(url);
object_spider.request_url();
object_spider.file_write("./image1.content", object_spider.request_get.content);