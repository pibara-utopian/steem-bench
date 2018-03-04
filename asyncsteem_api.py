#!/usr/bin/python
from twisted.internet import reactor
from twisted.logger import Logger, textFileLogObserver
from datetime import datetime as dt
import dateutil.parser
import sys
import time
from asyncsteem import RpcClient

dvcount = 0


def get_block(blk,log):
    def process_block(event, client):
        global dvcount
        if event != None:
            for t in event["transactions"]:
                for o in t["operations"]:
                    if o[0] == "vote" and o[1]["weight"] < 0:
                        dvcount = dvcount + 1
                        if dvcount % 250 == 0:
                            log.info("Processed {dv!r} downvotes",dv=dvcount)
    opp = rpcclient.get_block(blk)
    opp.on_result(process_block)

starttime = time.time()
obs = textFileLogObserver(sys.stdout)
log = Logger(observer=obs,namespace="asyncsteem_bench_nobatch")
rpcclient = RpcClient(reactor,log,nodelist="bench7",stop_when_empty=True)
for block in range(18581583,18610152):
    get_block(block,log)
rpcclient()
reactor.run()
endtime = time.time()
print "dvcount = ", dvcount
print "Processing January first of 2018 took", endtime-starttime,"seconds"
