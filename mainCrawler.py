#
# Start WebCrawler to generate DB
#
import os
import shutil

from Crawlers.CrawlerFactory import CrawlerFactory

# configure WebPages and Cawl-Mode
from Crawlers.HelperForCrawler import convert_workdir_to_json


pages = [

    # {'url': 'https://www.sms.at/smartzone/sms-sprueche/blondinenwitze-59/', 'type': 'joke', 'crawler': 'smsat'},
    # {'url': 'https://www.sms.at/smartzone/sms-sprueche/chuck-norris-facts-1093/', 'type': 'cn', 'crawler': 'smsat'},
    # {'url': 'https://www.sms.at/smartzone/sms-sprueche/spassiges-allerlei-19/', 'type': 'joke', 'crawler': 'smsat'},
    # {'url': 'https://www.sms.at/smartzone/sms-sprueche/weisheiten-37/', 'type': 'joke', 'crawler': 'smsat'},
    # {'url': 'https://www.sms.at/smartzone/sms-sprueche/zitate-60/', 'type': 'citate', 'crawler': 'smsat'},
    # {'url': 'https://www.deutsch-lernen.com/witze.php', 'type': 'joke', 'crawler': 'deutschlernen'},
    # {'url': 'http://witze.net/alle-kinder-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/arbeit-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/auto-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/chef-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/chuck-norris-witze', 'type': 'cn', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/corona-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/ddr-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/deutsche-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/lehrer-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/reime-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/tiere-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/schwarzer-humor-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/unterschied-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/weihnachten-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/winter-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'http://witze.net/%c3%b6sterreich-witze', 'type': 'citate', 'crawler': 'witzenet'},
    # {'url': 'https://karrierebibel.de/witze/', 'type': 'joke', 'crawler': 'justli', 'options': 'liwithoutclass'},
    # {'url': 'https://www.aberwitzig.com/flachwitze.php', 'type': 'joke', 'crawler': 'justhr', 'mainelement': 'div',
    #     'mainelementclass': 'haupt', 'stopelement': 'a', 'linkelementid': 'topeinhundert', 'linkfallbackclass': 'rot'},
    # {'url': 'https://www.aberwitzig.com/schwarzer-humor.php', 'type': 'joke', 'crawler': 'justhr', 'mainelement': 'div',
    #     'mainelementclass': 'haupt', 'stopelement': 'a', 'linkelementid': 'topeinhundert', 'linkfallbackclass': 'rot'},
    # {'url': 'https://www.aberwitzig.com/coole-lustige-sprueche.php', 'type': 'joke', 'crawler': 'justhr',
    #     'mainelement': 'div', 'mainelementclass': 'haupt', 'stopelement': 'a', 'linkelementid': 'topeinhundert',
    #     'linkfallbackclass': 'rot'},
    # {'url': 'https://www.aberwitzig.com/scherzfragen.php', 'type': 'joke', 'crawler': 'justhr',
    #     'mainelement': 'div', 'mainelementclass': 'haupt', 'stopelement': 'a', 'linkelementid': 'topeinhundert',
    #     'linkfallbackclass': 'rot'},
    # {'url': 'https://www.aberwitzig.com/gute-witze.php', 'type': 'joke', 'crawler': 'justhr',
    #     'mainelement': 'div', 'mainelementclass': 'haupt', 'stopelement': 'a', 'linkelementid': 'topeinhundert',
    #     'linkfallbackclass': 'rot'},
    # {'url': 'https://www.aberwitzig.com/alle-kinder-witze.php', 'type': 'joke', 'crawler': 'justhr',
    #     'mainelement': 'div', 'mainelementclass': 'haupt', 'stopelement': 'a', 'linkelementid': 'topeinhundert',
    #     'linkfallbackclass': 'rot'},


    {'url': 'https://witze.at/kategorie/7/auto/', 'type': 'joke', 'crawler': 'witzat' },
]

# configure folders (must already exist)
WORKDIR = "C:/temp/GermanFunDB/Temp"
EXPORTFILE = "C:/temp/GermanFunDB/GermanFunDB.json"

# ============================================
# Start of ProgramCode, no adjustment required
# ============================================

# cleanup workdir
if os.path.exists(WORKDIR):
    shutil.rmtree(WORKDIR)

# start crawling
for param in pages:
    param["workdir"] = WORKDIR
    crawler = CrawlerFactory.get_crawler(param)
    crawler.start()

# creating output
convert_workdir_to_json(EXPORTFILE, WORKDIR)


