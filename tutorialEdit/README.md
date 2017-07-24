Using the Web Scraper:

1.  Before you run this program, it is reccommended that you run it behind a vitual environment. If you do not already have one setup, simple instructions can be found here: notes.webutvikling.org/get-python-virtualenv-pip-without-sudo/ to make it work on the flip server, however instead of merely typing 'source activate', you may have to type 'source activate.csh' to activate your virutal environment.
2.  Once your environment is active, now install the Scrapy package: pip install Scrapy.   
3.  Once that is done, cd into tutorialEdit.
4.  Type 'scrapy crawl ikea.com -o output2.JSON -t json' 
5.  cat output2.JSON to see the links.
5.  This scrapes all the links on the http://ikea.com homepage but it doesn't follow them.  To do that edit the tutorialEdit/tutorial/spiders/quotes_spider.py file and change follow=False to True on line 34.
6.  This will follow the links as well as scrape them. You will want to ctrl+c to stop it from following the links.
