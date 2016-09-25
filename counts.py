import time
from get_info import enterprise_info

while True:
    print(enterprise_info.find().count())
    time.sleep(5)