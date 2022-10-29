import json
import os
import datetime
import requests
from pathlib import Path
from bs4 import BeautifulSoup, Tag, ResultSet

from Crawlers.HelperForCrawler import get_indexed_element_from_string


class CrawlerBase:
    """Base Crawler class for extraction of jokes from a joke page

    This File is part of GermanFunDB, a German Fun Database for ML Projects

    GermanFunDB requres beautifulsoap4 for operations
    """

    def __init__(
            self,
            fun_db,
            param
    ):
        """Constructor.

        :param fun_db: initialilzed fun_db for storing information
        :param param: parameters given as dictionary with at least url and type

        Possible Type(s):
            joke (Just a Joke)
            jn (Juck Norris Style)
            citate (Joke with citation)
        """

        # check if cricical params exist and store them
        if param is None or param.get("url", None) is None or param.get("type", None) is None:
            raise Exception("Param does not exist or missing params")

        self.param = param

        # initialize some other attributes
        self.soupcontent = None
        self.currenturl = None
        self.oldprocessedlinks = None
        self.possiblelinklist = []

        # check if we have to serch for author
        self.fetch_author = self.param.get("type", None) == "citate"
        self.fun_db = fun_db


    def start(self, url=None):
        """start crawling incl. preparation

        :param url: the web-url where to start crawling
        """
        # if url was missing, start with url from self.param
        if url is None:
            url = self.param.get("url", None)

        # prepare funDB and switch workdir
        next_web_index = self.fun_db.get_next_index_from_file("/webidx")
        self.fun_db.switch_jokedir("/web_" + str(next_web_index))

        # write information of web
        information = {
            "param": self.param,
            "timestamp": str(datetime.datetime.now())
        }
        self.fun_db.write_info(information)

        print("Start working on " + url)

        # start crawling
        self.crawl(url)

    def crawl(self, url, recurse = True):
        """do the crawl, necessary preparations-steps have to be done before

        :param url: the web-url where to crawl from
        """

        self.currenturl = url

        # stop if no content could be loaded
        if self.get_pagecontent(url) is None:
            return None

        # find and extract jokes
        self.load_and_save_jokes()

        if not recurse:
            return

        # search for follow-up url
        next_url = self.find_followinglink()
        while next_url:
            print("  Continue on: " + next_url)
            self.crawl(next_url, recurse=False)
            next_url = self.find_followinglink()

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

    def return_possible_link(self):
        """return a possible link from self.possiblelinklist

        :return: possible link or None if no one was found
        """

        # as long as there are some links left in list
        while len(self.possiblelinklist) > 0:
            # fetch first element from self.possiblelink
            possiblelink = self.possiblelinklist[0]
            self.possiblelinklist.remove(possiblelink)

            # try if it is a newly seen link
            if possiblelink not in self.oldprocessedlinks:
                self.oldprocessedlinks.append(possiblelink)
                return possiblelink

        # Nothing found!
        return None

    def possiblelinklist_append(self, list):
        """Append a given list of a-tags to the self.possiblelinklist

        :param list: list of a Tags to be added to self.possiblelinklist
        """

        for link in list:
            if not isinstance(link, Tag):
                # ignore others than Tags
                continue

            # get and prepare url
            href = link.get('href')
            possiblelink = self.get_full_url(href)

            # try to store in list
            if possiblelink not in self.oldprocessedlinks:
                self.possiblelinklist.append(possiblelink)


    def get_sequence_of_element(self, start_element, element_type):
        """Starts with a start element and gets all next_elements that are of given element_type

        :param start_element: start element (type Tag)
        :param element_type: element-name that are required
        :return: the list of elements
        """

        # initialisation and check params
        list = []
        if start_element is None or element_type is None:
            return None

        if isinstance(start_element, ResultSet):
            # start_element is ResultSet, e.g. result of find_all ==> process each element and finish
            for element in start_element:
                listPart = self.get_sequence_of_element(element, element_type)
                list.extend(listPart)
            return list

        if not isinstance(start_element, Tag):
            return None

        # append element and next_elements of requested type to list
        list.append(start_element)
        for e in start_element.next_elements:
            if isinstance(e, Tag):
                if e.name == "a":
                    list.append(e)
                else:
                    # we found something else, stop here
                    break

        return list

    def get_full_url(self, urlpart):
        """gets a working url from a possible url-part compaired to self.currenturl

        :param urlpart: the (possible) part of an url
        """

        if urlpart is None:
            return urlpart

        # if url starts with http or https, all is good
        if urlpart[:5] == "http:" or urlpart[:6] == "https:":
            return urlpart

        # if url starts with / we have to extract servername
        # since url is always in format http://servername/ or https://servername/,
        # we have to find 3rd slash
        if urlpart[0] == "/":
            end_of_servername = get_indexed_element_from_string(self.currenturl, "/", 3)
            if end_of_servername == -1:
                return None
            return self.currenturl[:end_of_servername] + urlpart

        # last try: concat urlpart at the end of url_base but split filename from urlbase in advance
        lastslash = self.currenturl.rfind("/")
        url_base_without_file = self.currenturl
        if lastslash >= 0:
            url_base_without_file = self.currenturl[:lastslash]
        return url_base_without_file + "/" + urlpart
