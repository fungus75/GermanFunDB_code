#
# Start WebCrawler to generate DB
#
from Data.Joke import Joke

# configure WebPages and Cawl-Mode
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

# Start of ProgramCode, no adjustment required
joke = Joke("Hallo, ich bin ein Witz2")
joke.save_as_file("c:/temp/x.json")

joke2 = Joke(import_filename="c:/temp/x.json")
print(joke2.to_jsonstring())

