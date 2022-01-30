from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.HelperForCrawler import save_joke_and_update_index, get_full_url, get_author_from_end, \
    remove_unnecessary_spaces
from Data.Joke import Joke


class CrawlerJustli(CrawlerBase):
    """Crawler for varous pages that store jokes in "li"-Elements

    Use param["options"] for additional options:
    * liwithoutclass => only the li with no css-class set

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        return None

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        liwithoutclass = self.param.get("options", None) == "liwithoutclass"

        # find div where jokes are stored
        lis = self.soupcontent.find_all("li")

        for element in lis:
            if liwithoutclass and element.get('class', None) is not None:
                continue
            text = element.text
            author = None

            # if we have to fetch author, find within last brackets
            if self.fetch_author:
                textauthor = get_author_from_end(text, '~')
                text = textauthor["text"]
                author = textauthor["author"]

            joke = Joke(text, author)
            save_joke_and_update_index(joke, self.jokeworkfolder)




