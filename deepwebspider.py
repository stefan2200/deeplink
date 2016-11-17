import os
import re
import urllib2
import sys
import time
import pymysql.cursors


class dws:
    found = None
    connection = None
    queue = None
    name = None
    sleeptime = 2
    keeprunning = True
    state = 1
    def run(self):
        while(self.keeprunning):
            if len(self.queue) > 0:
                self.state = 1
                u = self.queue.pop(0)
                self.found.append(u)
                self.gethost(u)
            else:
                print "[%s] [T]" % self.name
                self.state = 0
            time.sleep(self.sleeptime)

    def addHost(self, orgurl, url, title, sublinks, server):
        try:
            cur = self.connection.cursor()
            cur.execute("INSERT INTO hosts(`host`, `url`, `title`, `firstseen`, `lastseen`, `found_links`, `server`) VALUES (%s, %s, %s, NOW(), NOW(), %s, %s)", (self.stripHost(orgurl), url, title, sublinks, server))
            self.connection.commit()
            return True
        except:
            print "Database error for entry %s" % url
            return False
    def stripHost(self, url):
        rtn = re.search('(http\://[a-z0-9]+\.onion)', url)
        if rtn and rtn.group(1):
            return rtn.group(1)
        return url
    def getlinks(self, pagebody):
        links = []
        pattern = re.compile('(http\://[a-z0-9]+\.onion)')
        for m in re.finditer(pattern, pagebody):
            links.append(m.group(1))
        return links
    def getTitle(self, pagebody):
        rtn = re.search('<title>(.+?)<\/title>', pagebody)
        if rtn and rtn.group(1):
            return rtn.group(1)
        return None
    def addlinks(self, links):
        num = 0
        for l in links:
            if l not in self.queue and l not in self.found:
                self.queue.append(l)
                num += 1
        print "[%s] [Q] %s" % (self.name, num)
        return num

    def gethost(self, url):
        if not url.endswith('/'): url = url + "/"
        print "[%s] [G] %s " % (self.name, url)
        req = None
        try:
            req = urllib2.urlopen(url)
            resp = req.read()
            getlinks = self.getlinks(resp)
            numlinks = self.addlinks(getlinks)
            server = "Unknown"
            if "server" in dict(req.info()):
                server = dict(req.info())['server']
            if self.addHost(url, req.geturl(), self.getTitle(resp), numlinks, server):
                print "[%s] [A] %s [%d/%d]" % (self.name, url, len(self.queue), len(self.found))

        except:
            if req:
                req.close()
            print "[%s] [E] %s" % (self.name, url)

