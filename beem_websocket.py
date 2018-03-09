#!/usr/bin/python3
import beem
from beem.blockchain import Blockchain
import time
nodes = ["wss://steemd.pevo.science"]
threading = True
thread_num = 16
stm = beem.steem.Steem(nodes)
b = Blockchain(steem_instance=stm)
starttime = time.time()
dvcount = 0
firstblock = 18581583
while True:
    lastblock = firstblock + 100
    if lastblock > 18610152:
        lastblock = 18610152
    blocks = b.blocks(firstblock, lastblock, threading=threading, thread_num=thread_num)
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

