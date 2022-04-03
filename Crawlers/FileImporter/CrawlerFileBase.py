import json
import time

import requests

from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.Translators.simpleDeepLTranslate import simpleDeepLTranslate
from Crawlers.Translators.simpleGoogleTranslate import simpleGoogleTranslate
from Crawlers.HelperForCrawler import get_author_from_end, remove_unnecessary_spaces
from Data.Joke import Joke


class CrawlerFileBase(CrawlerBase):
    """Crawler for csv-import

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        # no followup
        return None

    def crawl(self, url):
        """do the crawl, necessary preparations-steps have to be done before

        :param url: the file where to crawl from
        """
        self.currenturl = url

        # find and extract jokes
        self.load_and_save_jokes()





