#
# Start WebCrawler to generate DB
#
import os
import shutil
import configuration as cfg

from Crawlers.CrawlerFactory import CrawlerFactory
from FunDB.FunDB import FunDB

# cleanup workdir
if os.path.exists(cfg.WORKDIR):
    shutil.rmtree(cfg.WORKDIR)

# Initialize FunDB
fun_db = FunDB(cfg.WORKDIR)

# import old state of db
fun_db.import_workdir(cfg.IMPORTDIR)

# start crawling
for param in cfg.pages:
    crawler = CrawlerFactory.get_crawler(fun_db, param)
    crawler.start()

