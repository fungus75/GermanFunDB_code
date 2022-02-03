from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.HelperForCrawler import get_author_from_end
from Data.Joke import Joke


class CrawlerWitzenet(CrawlerBase):
    """Crawler for witze.net

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find all links
        links = self.soupcontent.find_all("a", {"class": "x-xButton"})
        next_url = None
        for link in links:
            if link.text.strip()[:7] == "Nächste":
                next_url = link.get('href')
        return self.get_full_url(next_url)

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # find div where jokes are stored
        divs = self.soupcontent.find_all("div", {"class": "joke"})

        for div in divs:
            text = div.text
            author = None

            # if we have to fetch author, find within last brackets
            if self.fetch_author:
                textauthor = get_author_from_end(text, '~')
                text = textauthor["text"]
                author = textauthor["author"]

            joke = Joke(text, author)
            self.fun_db.save_joke_and_update_index(joke)




