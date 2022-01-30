import json
import os
import datetime;
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from Crawlers.HelperForCrawler import get_next_index_from_file


class CrawlerBase:
    """Base Crawler class for extraction of jokes from a joke page

    This File is part of GermanFunDB, a German Fun Database for ML Projects

    GermanFunDB requres beautifulsoap4 for operations
    """

    def __init__(
            self,
            param
    ):
        """Constructor.

        :param param: parameters given as dictionary with at least url and type

        Possible Type(s):
            joke (Just a Joke)
            jn (Juck Norris Style)
            citate (Joke with citation)
        """

        # check if cricical params exist and store them
        if param is None or param.get("url",None) is None or param.get("type",None) is None:
            raise Exception("Param does not exist or missing params")

        self.param = param

        # initialize some other attributes
        self.soupcontent = None
        self.webworkfolder = None
        self.currenturl = None

    def start(self, url=None):
        """start crawling incl. preparation

        :param url: the web-url where to start crawling
        """
        # if url was missing, start with url from self.param
        if url is None:
            url = self.param.get("url", None)

        self.currenturl = url

        # prepare workfolder for current task
        path = Path(self.param.get("workdir"))
        path.mkdir(parents=True, exist_ok=True)
        next_web_index = get_next_index_from_file(self.param.get("workdir") + "/webidx")
        self.webworkfolder = self.param.get("workdir") + "/web_" + str(next_web_index)
        os.mkdir(self.webworkfolder)

        # write information of web
        information = {
            "param": self.param,
            "timestamp": str(datetime.datetime.now())
        }
        infofile = open(self.webworkfolder + "/info", "w")
        infofile.write(json.dumps(information))
        infofile.close()

        print("Start working on " + url)

        # start crawling
        self.crawl(url)

    def crawl(self,url):
        """do the crawl, necessary preparations-steps have to be done before

        :param url: the web-url where to crawl from
        """

        # stop if no content could be loaded
        if self.get_pagecontent(url) is None:
            return None

        # find and extract jokes
        self.load_and_save_jokes()

        # search for follow-up url
        next_url = self.find_followinglink()
        if next_url is not None:
            print("  Continue on: " + next_url)
            self.crawl(next_url)

    def get_pagecontent(self, url):
        """returns the content of a page directly and stores it in self.soupcontent

        :param url: url to load
        :return: content of page as beautifulsoap-object
        """

        # fetch url
        page = requests.get(url)
        if page.status_code != 200:
            return None

        # convert ot beautifulsoup
        self.soupcontent = BeautifulSoup(page.content, "html.parser")
        return self.soupcontent

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        Must be overloaded in each Crawler-Subclass

        :return: follow-up url or None if no one found
        """
        raise Exception("Using CrawlerBase directly is not supported")

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        Must be overloaded in each Crawler-Subclass

        """
        raise Exception("Using CrawlerBase directly is not supported")


