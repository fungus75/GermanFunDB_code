import json
import time
import requests
import gzip

from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.Translators.simpleGoogleTranslate import simpleGoogleTranslate
from Crawlers.HelperForCrawler import get_author_from_end, remove_unnecessary_spaces
from Data.Joke import Joke


class CrawlerTranslaterJokesData(CrawlerBase):
    """Crawler for deutsch-lernen.com

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        # no followup
        return None

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        srclang = self.param.get("srclang", None)
        if srclang is None:
            raise Exception("Parameter srclang not set")


        # get directly from url
        page = requests.get(self.currenturl)
        if page.status_code != 200:
            return Exception("Can not get content from url " + self.currenturl)


        # unzip data
        content = gzip.decompress(page.content).decode('utf-8')

        # split by newline
        data = content.split("\n")

        # parse one by one
        for oneJoke in data:

            # each line has that format: humor-level \t joke
            # humor-level can be seen as number of likes, because the more the better.
            joke_parts = oneJoke.split("\t")


            # wait 3 seconds to not over-use api
            time.sleep(3)

            # translate text from srclang to german
            text = simpleGoogleTranslate(joke_parts[1], srclang, "de")
            text = remove_unnecessary_spaces(text)
            print(text)
            author = None

            joke = Joke(text, author, likes=joke_parts[0])
            self.fun_db.save_joke_and_update_index(joke)





