How to use the Perseus-keyword_search Spider

0.  If you are not publishing yet, it is recommended that you install scrapy behind a vitual environment. If you do not already have one setup, simple instructions can be found here: notes.webutvikling.org/get-python-virtualenv-pip-without-sudo/ to make it work on the flip server, however instead of merely typing 'source activate', you may have to type 'source activate.csh' to activate your virutal environment.
1.  Be sure that the web scraper is installed- "npm install scrapy"
2.  From the command line: 
3.  Breadth First Search-
scrapy crawl keyword_search -a start_url=<url> -a find_word=<target-word> -s CLOSESPIDER_PAGECOUNT=<max pages> -o <filename>.JSON -t json
		eg. scrapy crawl keyword_search -a start_url=http://ikea.com -a find_word=share -s CLOSESPIDER_PAGECOUNT=35 -o output.JSON -t json
4.  Depth First Search-
scrapy crawl keyword_search -a start_url=<url> -a find_word=<target-word> -s CLOSESPIDER_PAGECOUNT=<max pages> -s DEPTH_PRIORITY=1 -s SCHEDULER_DISK_QUEUE='scrapy.squeues.PickleFifoDiskQueue' -s SCHEDULER_MEMORY_QUEUE='scrapy.squeues.FifoMemoryQueue' -o <filename>.JSON -t json
eg. scrapy crawl washington.edu -a start_url=http://ikea.com -a find_word=share -s CLOSESPIDER_PAGECOUNT=35 -s DEPTH_PRIORITY=1 -s SCHEDULER_DISK_QUEUE='scrapy.squeues.PickleFifoDiskQueue' -s SCHEDULER_MEMORY_QUEUE='scrapy.squeues.FifoMemoryQueue' -o output.JSON -t json
5.  cat <output file> to see your links		
