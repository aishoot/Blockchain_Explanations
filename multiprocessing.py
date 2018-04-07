import urllib2
from multiprocessing import Pool   # 多进程
from multiprocessing.dummy import Pool as ThreadPool  # 多线程

urls = ["https://wew.com", "https://www.baidu.com"]

pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
