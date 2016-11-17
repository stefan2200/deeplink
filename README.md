# deeplink
Multi-Threaded Deep web Spider
Written in Python (Tested Python on 2.7)
Required:
	- Python 2.7.x
	- PyMYSQL
	- Working MySQL server

Change connection properties in deeplink.py and import MySQL table set-up in your database.

Usage: python deeplink.py [number of threads]
Default of 5 threads will be used if no custom variable is set.

Uses links on union domains to discover hidden services, start url is currently hiddenwiki clear net portal, additional start url's can be added.
Default set-up will find +/- 4.5K services.

Still a very w.i.p. but it's something :)
