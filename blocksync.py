#!/usr/bin/python3
import time
from blocksync import Blocksync

s = Blocksync(endpoints=['https://api.steemitstage.com'])
starttime=time.time()
dvcount = 0
for block in s.get_block_stream(start_block=18581583):
    for t in block["transactions"]:
        for o in t["operations"]:
            if o[0] == "vote" and o[1]["weight"] < 0:
                dvcount = dvcount + 1
                if dvcount % 250 == 0:
                    print("Processed",dvcount)
    if block["height"] == 18610151:
        break;
endtime = time.time()
print("dvcount = ", dvcount)
print("Processing January first of 2018 took", endtime-starttime,"seconds")

