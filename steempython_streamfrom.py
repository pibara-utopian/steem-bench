#!/usr/bin/python3
import steem
import time
nodes = ["https://steemd.pevo.science/"]
steemd = steem.steemd.Steemd(nodes) #FIXME, issue with using stage, no clue as to why.
#steemd = steem.steemd.Steemd()
blockchain = steem.blockchain.Blockchain(steemd)
starttime = time.time()
downvotes = 0
for entry in blockchain.stream_from(18581583):
    block_no = entry["block"]
    if block_no >= 18610152:
        break
    op = entry["op"]
    if op[0] == "vote":
        if op[1]["weight"] < 0:
            downvotes = downvotes + 1
            if downvotes % 250 == 0:
                print("Processed",downvotes,"downvotes so far")
endtime = time.time()
print("dvcount = ", downvotes)
print("Processing January first of 2018 took", endtime-starttime,"seconds")

