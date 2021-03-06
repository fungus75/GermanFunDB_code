import time

from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.HelperForCrawler import remove_unnecessary_spaces, get_author_from_top
from Data.Joke import Joke


class CrawlerWitzeat(CrawlerBase):
    """Crawler for WITZE.AT

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        next_url = None

        # find navigation element
        navs = self.soupcontent.find_all("nav")
        if navs is None:
            return None

        # search all navs
        for nav in navs:
            # find li with class pagination-button-next
            li = nav.find("li", {"class": "pagination-button-next"})
            if li is None:
                continue

            # find all links
            link = li.find("a")
            next_url = link.get('href', None)

        time.sleep(3)  # Sleep for 3 seconds to not flood webpage

        return self.get_full_url(next_url)

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find relevant element
        article = self.soupcontent.find("article")
        if article is None:
            return
        p = article.find("p")
        if p is None:
            return

        # Extract text
        text = remove_unnecessary_spaces(p.text)
        author = None

        # if we have to fetch author, find within last brackets
        if self.fetch_author:
            textauthor = get_author_from_top(text, None, ':')
            text = textauthor["text"]
            author = textauthor["author"]

        # Save Joke
        joke = Joke(text, author)
        self.fun_db.save_joke_and_update_index(joke)




