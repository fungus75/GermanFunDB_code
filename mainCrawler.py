#
# Start WebCrawler to generate DB
#
import os
import shutil

from Crawlers.CrawlerFactory import CrawlerFactory

# configure WebPages and Cawl-Mode
from Crawlers.HelperForCrawler import convert_workdir_to_json

pages = [{'url': 'https://www.sms.at/smartzone/sms-sprueche/blondinenwitze-59/', 'type': 'joke', 'crawler': 'smsat'},
         {'url': 'https://www.sms.at/smartzone/sms-sprueche/chuck-norris-facts-1093/', 'type': 'jn',
          'crawler': 'smsat'},
         {'url': 'https://www.sms.at/smartzone/sms-sprueche/spassiges-allerlei-19/', 'type': 'joke',
          'crawler': 'smsat'},
         {'url': 'https://www.sms.at/smartzone/sms-sprueche/weisheiten-37/', 'type': 'joke', 'crawler': 'smsat'},
         {'url': 'https://www.sms.at/smartzone/sms-sprueche/zitate-60/', 'type': 'citate', 'crawler': 'smsat'},
         ]

# configure folders (must already exist)
WORKDIR = "C:/temp/GermanFunDB/Temp"
EXPORTFILE = "C:/temp/GermanFunDB/GermanFunDB.json"

# ============================================
# Start of ProgramCode, no adjustment required
# ============================================

# cleanup workdir
#if os.path.exists(WORKDIR):
#    shutil.rmtree(WORKDIR)

# start crawling
#for param in pages:
#    param["workdir"] = WORKDIR
#    crawler = CrawlerFactory.get_crawler(param)
#    crawler.start()

# creating output
convert_workdir_to_json(EXPORTFILE, WORKDIR)


