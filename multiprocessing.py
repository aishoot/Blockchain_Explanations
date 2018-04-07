# A few lines of python code to implement parallel computing
from multiprocessing import Pool   # multi-process
from multiprocessing.dummy import Pool as ThreadPool   # multi-thread

urls = ["https://wew.com", "https://www.baidu.com"]

pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
