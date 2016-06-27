import time, os
from common.redis import redisPublishMessage

class Tail(object):

    def __init__(self, path_log, path_name):

    	self.path_log = path_log

        self.path_name = path_name

def TailLog(path_log, path_name):

		log = open(path_log + path_name,'r')

		while 1:
		    where = log.tell()
		    line = log.readline()
		    if not line:
		        time.sleep(1)
		        log.seek(where)
		    else:
		        redisPublishMessage(line), 