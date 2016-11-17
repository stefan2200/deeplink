import pymysql.cursors
import re
import sys
import os
import threading
from deepwebspider import dws
import time
spiders = []
class spider(threading.Thread):
    dws = None
    def __init__(self, conn, found, queue, name):
        threading.Thread.__init__(self)
        self.dws = dws()
        self.dws.connection = conn
        self.dws.found = found
        self.dws.queue = queue
        self.dws.name = name
    def run(self):
        self.dws.run()




mainqueue = ['https://thehiddenwiki.org/']
foundqueue = []
threads = 5
try:
    threads = int(sys.argv[1])
except:
    print "No threadnum detected, using default of %d instead" % threads
print "Welcome, this script automaticly indexes .onion addresses trough linked sites, \nThread messages: \n[G] Getting url\n[T] Timeout, no url's in queue\n[E] Connection or socket error\n[A] Added to database\n[Q] Numner of url's added to queue"
print "Starting %d threads" % threads
for x in range(0, threads):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',
                                 db='deepweb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    s = spider(connection, foundqueue, mainqueue, "Thread-%s" % (x +1) )
    s.daemon = True
    s.start()
    spiders.append(s)
time.sleep(10)
while True:
    try:
        time.sleep(0.1)
        working = 0
        for x in spiders:
            if x.dws.state is 1:
                working += 1
        if working is 0:
            print "All spiders in timeout state, script done"
            for x in spiders:
                x.dws.keeprunning = False
            break

    except:
        print "Exit detected, stopping threads!"
        for x in spiders:
            x.dws.keeprunning = False
print "Goodbye :)"