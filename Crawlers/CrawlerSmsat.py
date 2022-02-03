from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.HelperForCrawler import get_author_from_end
from Data.Joke import Joke


class CrawlerSmsat(CrawlerBase):
    """Crawler for SMS.AT

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find all navigation table
        navtable = self.soupcontent.find("table", {"class": "page_navigation"})
        if navtable is None:
            return None

        # find all links
        links = navtable.find_all("a")
        next_url = None
        for link in links:
            if link.text.strip() == "Weiter":
                next_url = link.get('href')
        return self.get_full_url(next_url)

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find all relevant divs
        jokedivs = self.soupcontent.find_all("div", {"class": "sms_item_text"})

        # get text of each joke and crate new joke
        for onediv in jokedivs:
            text = onediv.text.strip()
            author = None

            # if we have to fetch author, find within last brackets
            if self.fetch_author:
                textauthor = get_author_from_end(text, '(', ')')
                text = textauthor["text"]
                author = textauthor["author"]

            joke = Joke(text, author)
            self.fun_db.save_joke_and_update_index(joke)




