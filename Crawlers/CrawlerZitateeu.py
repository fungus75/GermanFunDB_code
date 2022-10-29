from Crawlers.CrawlerBase import CrawlerBase
from Data.Joke import Joke
from bs4 import Tag, ResultSet
from Crawlers.HelperForCrawler import get_author_from_end, remove_unnecessary_spaces


class CrawlerZitateeu(CrawlerBase):
    """Crawler for zitate.eu

    """

    def __init__(
            self,
            fun_db,
            param
    ):
        super().__init__(fun_db, param)
        self.topics = None

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        if self.oldprocessedlinks is None:
            self.oldprocessedlinks = [self.currenturl]

        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # check if topics exist
        if self.topics is None:
            links = self.soupcontent.find_all("a")
            self.topics = []
            for link in links:
                if not isinstance(link, Tag):
                    continue
                href = link.get('href')
                if href.startswith("/topic/"):
                    self.topics.append(href)
                    self.possiblelinklist_append([link])

        # check if next exist
        next = self.soupcontent.find("li",{"class":"next"})
        if next is not None:
            link = next.find("a")
            self.possiblelinklist_append([link])

        # return one good element of possiblelinklist
        return self.return_possible_link()

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find ul where author is stored
        portfolioList = self.soupcontent.find("ul",{"class":"portfolio-list"})
        if portfolioList is None:
            return

        lis = portfolioList.findAll("li",{"class":"col-md-12"})

        for li in lis:
            author = None

            if self.fetch_author:
                ah4=li.find("h4")
                author = remove_unnecessary_spaces(ah4.text)

            txtdiv = li.find("div", {"class": "zitate-list-text"})
            text = remove_unnecessary_spaces(txtdiv.text)


            joke = Joke(text, author)
            self.fun_db.save_joke_and_update_index(joke)




