#!/usr/bin/python3
import time
from blocksync import Blocksync

s = Blocksync(endpoints=['https://api.steemitstage.com'])
starttime=time.time()
dvcount = 0
for op in s.get_op_stream(start_block=18581583, batch_size=100, whitelist=['vote']):
    if op["block_num"] > 18610151:
        break;
    if op["weight"] < 0:
        dvcount = dvcount + 1
        if dvcount % 250 == 0:
            print("Processed", dvcount, op['block_num'])
endtime = time.time()
print("dvcount = ", dvcount)
print("Processing January first of 2018 took", endtime-starttime,"seconds")
