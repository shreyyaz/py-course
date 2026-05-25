# def net_price(list_price,discount=0,tax=0.05):  #default value of discount is 0
#     return list_price*(1-discount)*(1+tax)

# print(net_price(500,0,0.5))
# print(net_price(500))

import time
# def count(start=0,end):  wont work PARAMETERS WITH DEFAULT VALUES MUST COME AFTER NORMAL PARAMETERS
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("TIME UP")

print(count(5))

