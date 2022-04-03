import time
import csv

from html.parser import HTMLParser
from Crawlers.FileImporter.CrawlerFileBase import CrawlerFileBase
from Crawlers.HelperForCrawler import get_author_from_end, remove_unnecessary_spaces
from Data.Joke import Joke


class CrawlerCSVImport(CrawlerFileBase):
    """Crawler for csv-import

    """

    def load_and_save_jokes(self):
        """Extract jokes directly from file

        """

        authorfield = self.param.get("authorfield", None)
        jokefield = self.param.get("jokefield", None)
        if jokefield is None:
            raise Exception("Parameter jokefield is a must!")

        eval_header = self.param.get("header", None) == "True"
        convert_html_entities = self.param.get("converthtmlentities", None) == "True"

        authorfieldindex = -1

        with open(self.currenturl) as csvfile:
            csvreader = csv.reader(csvfile,
                                   delimiter=self.param.get("delimiter", None),
                                   quotechar=self.param.get("quotechar", None))
            for row in csvreader:
                if eval_header:
                    eval_header = False
                    jokefieldindex = row.index(jokefield)
                    if authorfield is not None:
                        authorfieldindex = row.index(authorfield)
                    continue

                # extract joke
                text = row[jokefieldindex]
                text = remove_unnecessary_spaces(text)
                if convert_html_entities:
                    text = HTMLParser().unescape(text)
                print(text)
                author = None
                if authorfieldindex > -1:
                    author = row[authorfieldindex]

                joke = Joke(text, author)
                self.fun_db.save_joke_and_update_index(joke)





