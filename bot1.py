#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

argfile = str(sys.argv[1])
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

print('read')

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'SNgHvKkkYwxpGZcJiKTwPfDbv'
CONSUMER_SECRET = 'qaFXmZVZytrZrNeu3y0P5Fprx9sWQY66cjzjEMm3NjRozydlJI'
ACCESS_KEY = '3745260316-YbIuTAoAZrCf5nWxrlGLtiib2L2oClGNSMxJS3x'
ACCESS_SECRET = 'twnynteVz0XRBNlZjE6w69RxYllVTfe6sKXPBR2hAX6dL'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print('auth')

for line in f:
    print('new status: ' + line)
    api.update_status(status=line)
    print('posted!')
    time.sleep(300)#Tweet every 5 minutes

print('done')