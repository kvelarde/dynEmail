#!/usr/bin/env python
# example:
#   Must add your own ``apikey`` on line 22

import json
from datetime import datetime
from dynEmail import DynEmail

def createDict(item, id):
    """Make dict for easy json access"""
    d = {}
    d['text'] = item.strip()
    d['type'] = id
    return d


def main():
    '''Main Code execution'''
    # set time frame to get bounce now for the hell of it
    now = datetime.now()
    # I think this maks the months line up ehh
    if len(str(now.month)) == 1: dmonth = "0%s" % str(now.month)
    defaultdate = "%s-%s-%s" % (str(now.year),dmonth,str(now.day))

    d = DynEmail(apikey='your key here',
            startdate=defaultdate,
            enddate=defaultdate)

    # get bounces
    res = d.bouncemail().read()
    r = json.loads(res)
    l = []
    for m in r['response']['data']['bounces']:
        l.append( "Time: %s\n sender: %s: \n BounceRule: %s\n" % (m['bouncetime'],
            m['emailaddress'], m['bouncerule']) )

    # print showing users and timestamps in rows of thee
    for i in l: print i
 
if __name__ == '__main__':
    main()
