import os.path

from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.HelperForCrawler import save_joke_and_update_index, get_full_url
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
        return get_full_url(next_url, self.currenturl)

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        # check if we have to serch for author
        fetch_author = self.param.get("type", None) == "citate"

        # prepare workdir
        workdir = self.webworkfolder + "/jokes"
        if not os.path.exists(workdir):
            os.mkdir(workdir)

        # find all relevant divs
        jokedivs = self.soupcontent.find_all("div", {"class": "sms_item_text"})

        # get text of each joke and crate new joke
        for onediv in jokedivs:
            text = onediv.text.strip()
            author = None

            # if we have to fetch author, find within last brackets
            if fetch_author:
                lastBracket = text.rfind('(')
                if lastBracket >= 0:
                    author = text[lastBracket+1:].strip()
                    if author[-1] == ')':
                        author = author[:len(author)-1]
                    text = text[:lastBracket-1].strip()

            joke = Joke(text, author)
            save_joke_and_update_index(joke, workdir)




