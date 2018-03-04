steem-bench
===

This repo contains a set of simple scripts meant to perform a simple benchmark for python steem libraries. All scripts use one of two nodes (stage.steemit.com or api.steemit.com) and all scripts perform the same simple task. 

The task performed by each of the script is streaming all blocks from January 1st 2018 and counting downvotes for that day. The day in question starts with block 18581583 and ends with block 18610151. So what each script does is that it fetches these blocks, extracts the downvotes and counts them. The result for all scripts should be the same number, or there are broken scripts. If all scripts give the same result, the number of seconds needed to process the whole day should be a decent benchmark of the performance of the library. Please note though that node performance might fluctuate greatly over the day and there is no promise a node might not start to rate limit our benchmakr while in progress, so numbers should not be used to draw conclusions after only one run.


Some results:
===

* asyncsteem (stage, with batches)     :      4 minutes and 10 seconds.
* asyncsteem (stage, no batches)       :     17 minutes and 52 seconds. 
* asyncsteem (api, no batches)         :            
* steem-python (api, get\_blocks\_range) :  
* steem-python (api, stream\_from)      : 





