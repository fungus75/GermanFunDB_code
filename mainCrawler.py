#
# Start WebCrawler to generate DB
#
import os
import shutil

from Crawlers.CrawlerFactory import CrawlerFactory

# configure WebPages and Cawl-Mode
from Crawlers.HelperForCrawler import convert_workdir_to_json, import_into_workdir

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

    # {'url': 'https://witze.at/kategorie/7/auto/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/67/abkuerzungen/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/16/alle-kinder/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/59/bedienungsanleitungen/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/95/anti-witze/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/49/bei-gericht/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/3/berufe/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/64/chefwitze/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/45/computer/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/31/die-letzten-worte/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/55/graf-bobby/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/4/herr-ober/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/2/himmel-und-hoelle/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/26/in-der-schule/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/50/kannibalen/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/75/klassiker/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/47/microsoft-witze/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/42/musik/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/56/radio-eriwan/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/18/scherzfragen/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/79/schilder-aus-schilda/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/77/shoppingtour/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/8/sport/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/62/sprechende-namen-und-worte/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/89/studenten/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/25/tiere/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/94/vegetarier-und-veganer/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/91/verschwoerungstheorien/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/36/weihnachten/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/76/wilder-westen/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/71/wusstest-du/', 'type': 'joke', 'crawler': 'witzeat' },
]

# configure folders (must already exist)
WORKDIR = "C:/temp/GermanFunDB/Temp"
EXPORTFILE = "C:/temp/GermanFunDB/GermanFunDB.json"
IMPORTDIR = "C:/temp/GermanFunDB.stage/Temp"

# ============================================
# Start of ProgramCode, no adjustment required
# ============================================

# cleanup workdir
if os.path.exists(WORKDIR):
    shutil.rmtree(WORKDIR)

# import old state of db
import_into_workdir(IMPORTDIR, WORKDIR)

# start crawling
for param in pages:
    param["workdir"] = WORKDIR
    crawler = CrawlerFactory.get_crawler(param)
    crawler.start()

# creating output
convert_workdir_to_json(EXPORTFILE, WORKDIR)


