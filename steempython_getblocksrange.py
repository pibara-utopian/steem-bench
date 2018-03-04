#!/usr/bin/python3
import steem
import time
nodes = ["https://api.steemit.com"]
steemd = steem.steemd.Steemd(nodes)
starttime = time.time()
dvcount = 0
firstblock = 18581583
while True:
    lastblock = firstblock + 100
    if lastblock > 18610152:
        lastblock = 18610152
    blocks = steemd.get_blocks_range(firstblock,lastblock)
    for block in blocks:
        for t in block["transactions"]:
            for o in t["operations"]:
                if o[0] == "vote" and o[1]["weight"] < 0:
                    dvcount = dvcount + 1
                    if dvcount % 250 == 0:
                        print("Processed",dvcount)
    firstblock = lastblock
    if firstblock >= 18610152:
        break
endtime = time.time()
print("dvcount = ", dvcount)
print("Processing January first of 2018 took", endtime-starttime,"seconds")

