from bs4 import Tag

from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.HelperForCrawler import save_joke_and_update_index, get_full_url, get_author_from_end, \
    remove_unnecessary_spaces
from Data.Joke import Joke


class CrawlerDeutschlernen(CrawlerBase):
    """Crawler for deutsch-lernen.com

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find all navigation table
        navtable = self.soupcontent.find("div", {"id": "box"})
        if navtable is None:
            return None

        # find all links
        links = navtable.find_all("a")

        # search for link currently not processed
        if self.oldprocessedlinks is None:
            self.oldprocessedlinks = [self.currenturl]

        for link in links:
            href = link.get('href')
            if href[0:4] != "witz":
                continue

            possiblelink = get_full_url(href, self.currenturl)
            if possiblelink not in self.oldprocessedlinks:
                # found link that was not processed before
                self.oldprocessedlinks.append(possiblelink)
                return possiblelink

        return None

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find div where jokes start
        div_box = self.soupcontent.find("div", {"id": "box"})

        # walk through children until h3 is found
        for child in div_box.children:
            if isinstance(child, Tag) and child.name == "h3":
                for element in child.next_elements:
                    if isinstance(element, Tag) and element.name == "p":
                        text = remove_unnecessary_spaces(element.text)
                        break


                author = None

                # if we have to fetch author, find within last brackets
                if self.fetch_author:
                    textauthor = get_author_from_end(text)
                    text = textauthor["text"]
                    author = textauthor["author"]

                joke = Joke(text, author)
                save_joke_and_update_index(joke, self.jokeworkfolder)




