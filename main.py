from multiprocessing import Pool
from channel import channel_url
from get_info import x
from get_info import get_every_info

def get_all_info_from(channel):
    for i in range(1,100,1):
        get_every_info(channel,i)

if __name__ == '__main__':
    pool = Pool()
    for page in range(1, 100, 1):
        if x == 0:
            pool.map(get_all_info_from,channel_url)
        else:
            break