#
# Configuration for webcrawler and settings
#

# list of Pages to check and parameter/extractor
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

    # {'url': 'https://witze.at/kategorie/128/al-bundy-sprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/129/ausreden/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/157/bauernregeln/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/130/chuck-norris-facts/', 'type': 'cn', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/132/dieter-bohlen-sprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/162/freundschaftssprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/164/gute-nacht-sprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/167/hochzeitssprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/141/klosprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/169/kluge-sprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/171/lebensweisheiten/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/144/reime/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/151/trinksprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/187/vatertag-sprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/189/weihnachtssprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/190/whatsapp-sprueche/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/154/zungenbrecher/', 'type': 'joke', 'crawler': 'witzeat' },
    # {'url': 'https://witze.at/kategorie/73/zitate/', 'type': 'citate', 'crawler': 'witzeat' },
    # {'url': 'https://raw.githubusercontent.com/computational-humor/humor-recognition/master/data/FUN-dataset/assessed.json', 'type': 'joke', 'crawler': 'translate_fundataset', 'srclang': 'ru', 'translator': 'deepl'},
    # {'url': 'https://raw.githubusercontent.com/computational-humor/humor-recognition/master/data/FUN-dataset/test.json', 'type': 'joke', 'crawler': 'translate_fundataset', 'srclang': 'ru'},
    # {'url': 'https://github.com/orionw/rJokesData/raw/master/data/test.tsv.gz', 'type': 'joke', 'crawler': 'translate_rjokesdata', 'srclang': 'en'},
    {'url': 'C:/temp/GermanFunDB/schlechtewitzefront.csv', 'type': 'joke', 'crawler': 'csvimport', 'jokefield': 'witz',
     'header': 'True', 'delimiter': ',', 'quotechar':'"', 'converthtmlentities': 'True'}
]


#
# Directory/Filename configuration
#

# configure folder (must already exist) of main fun-database
WORKDIR = "C:/temp/GermanFunDB/Temp"

# Preload Database with existing staged database stored in that folder
IMPORTDIR = "C:/temp/GermanFunDB.stage/Temp"

# Export JSON File
EXPORTJSON = "C:/temp/GermanFunDB/GermanFunDB.json"

# Export CSV-File 1: List of sources
EXPORTCSVSOURCES = "C:/temp/GermanFunDB/GermanFunDB-Sources.csv"

# Export CSV-File 2: List of Jokes
EXPORTCSVDATA = "C:/temp/GermanFunDB/GermanFunDB-Data.csv"

# TXT File Export
EXPORTTXT = "C:/temp/GermanFunDB/GermanFunDB-OnlyJokes.txt"
