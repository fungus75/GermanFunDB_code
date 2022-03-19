import json
import time

import requests

from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.GoogleTranslate.simpleGoogleTranslate import simpleGoogleTranslate
from Crawlers.HelperForCrawler import get_author_from_end, remove_unnecessary_spaces
from Data.Joke import Joke


class CrawlerTranslateFUNDataset(CrawlerBase):
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


        # find div where jokes start
        data = json.loads(page.content)
        for oneJoke in data:

            # Joke is key, good/not good is value (!= 1 means not good)
            good = data[oneJoke]
            if good != 1:
                continue

            # wait 3 seconds to not over-use api
            time.sleep(3)

            # translate text from srclang to german
            text = simpleGoogleTranslate(oneJoke, srclang, "de")
            text = remove_unnecessary_spaces(text)
            print(text)
            author = None

            joke = Joke(text, author)
            self.fun_db.save_joke_and_update_index(joke)





