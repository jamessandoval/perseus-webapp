#!/usr/bin/env python

import flask
import os
import subprocess
from flask import send_from_directory
from flask_cors import CORS, cross_origin


# Create the application.
APP = flask.Flask(__name__)
CORS(APP)

#cors = CORS(APP, resources={r"/breadth": {"origins": "http://localhost:port"}})

# 127.0.0.1:33507/breadth/url/http://www.reddit.com/max/10/keyword/earth
@APP.route('/breadth/url/<path:url>/max/<int:max>/keyword/<string:keyword>')
def breadth(url, max, keyword):
    """ Displays the index page accessible at '127.0.0.1:33507'
    """
    pid = os.getpid()
    proc = subprocess.Popen(["ls"])
    newpid = str(proc.pid)
    max = str(max)

    os.system("scrapy crawl keyword_search -a start_url="+url+" -a find_word="+keyword+" -s CLOSESPIDER_PAGECOUNT="+max+" -o "+newpid+".JSON -t json") 
    root_dir = os.getcwd()

    
    #os.remove(newpid+'.JSON')
    response = send_from_directory(root_dir, newpid+'.JSON')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

# 127.0.0.1:33507/depth/url/http://www.reddit.com/max/10/keyword/earth
@APP.route('/depth/url/<path:url>/max/<int:max>/keyword/<string:keyword>')
def depth(url, max, keyword):
    """ Displays the index page accessible at '127.0.0.1:33507'
    """
    pid = os.getpid()
    proc = subprocess.Popen(["ls"])
    newpid = str(proc.pid)
    max = str(max)
    os.system("scrapy crawl keyword_search -a start_url="+url+" -a find_word="+keyword+" -s CLOSESPIDER_PAGECOUNT="+max+" -s DEPTH_PRIORITY=1 -s SCHEDULER_DISK_QUEUE='scrapy.squeues.PickleFifoDiskQueue' -s SCHEDULER_MEMORY_QUEUE='scrapy.squeues.FifoMemoryQueue' -o "+newpid+ ".JSON -t json") 

    root_dir = os.getcwd()
    
    #os.remove(newpid+'.JSON')
    response = send_from_directory(root_dir, newpid+'.JSON')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 443))
    APP.run()
