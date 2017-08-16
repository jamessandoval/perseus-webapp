#!/usr/bin/env python

import flask
import os
import subprocess
from flask import send_from_directory

# Create the application.
APP = flask.Flask(__name__)

# 127.0.0.1:5000/breadth/url/http://www.reddit.com/max/10/keyword/earth
@APP.route('/breadth/url/<path:url>/max/<int:max>/keyword/<string:keyword>')
def breadth(url, max, keyword):
    """ Displays the index page accessible at '127.0.0.1:5000'
    """
    pid = os.getpid()
    proc = subprocess.Popen(["ls"])
    newpid = str(proc.pid)
    max = str(max)

    os.system("scrapy crawl keyword_search -a start_url="+url+" -a find_word="+keyword+" -s CLOSESPIDER_PAGECOUNT="+max+" -o "+newpid+".JSON -t json") 
    root_dir = os.getcwd()

    
    #os.remove(newpid+'.JSON')
    return send_from_directory(root_dir, newpid+'.JSON')

# 127.0.0.1:5000/depth/url/http://www.reddit.com/max/10/keyword/earth
@APP.route('/depth/url/<path:url>/max/<int:max>/keyword/<string:keyword>')
def depth(url, max, keyword):
    """ Displays the index page accessible at '127.0.0.1:5000'
    """
    pid = os.getpid()
    proc = subprocess.Popen(["ls"])
    newpid = str(proc.pid)
    max = str(max)
    os.system("scrapy crawl keyword_search -a start_url="+url+" -a find_word="+keyword+" -s CLOSESPIDER_PAGECOUNT="+max+" -s DEPTH_PRIORITY=1 -s SCHEDULER_DISK_QUEUE='scrapy.squeues.PickleFifoDiskQueue' -s SCHEDULER_MEMORY_QUEUE='scrapy.squeues.FifoMemoryQueue' -o "+newpid+ ".JSON -t json") 

    root_dir = os.getcwd()
    
    #os.remove(newpid+'.JSON')
    return send_from_directory(root_dir, newpid+'.JSON')

if __name__ == '__main__':

    APP.debug=True
    APP.run()
