from bs4 import Tag

from Crawlers.CrawlerBase import CrawlerBase
from Crawlers.HelperForCrawler import get_author_from_end, remove_unnecessary_spaces
from Data.Joke import Joke


class CrawlerJusthr(CrawlerBase):
    """Crawler for varous pages that store jokes in "hr"-Elements

    Use param["options"] for additional options:
    * hrwithoutclass => only the hr with no css-class set

    Use param["mainelement"] for main element that stores jokes
    Use param["mainelementclass"] for css-class of main element that sores jokes
    Use param["stopelement"] for element where joke extraction should stop
    Use param["linkelementid"] for element where links are stored
    Use param["linkfallbackclass"] as fallback if no links were found (find all a-elements after the ones with that class

    """

    def find_followinglink(self):
        """Find and return follow-up-link in previously loaded soupcontent

        :return: follow-up url or None if no one found
        """

        if self.oldprocessedlinks is None:
            self.oldprocessedlinks = [self.currenturl]

        links = None

        # search links within param["linkelementid"]
        linkbase=self.soupcontent.find(id=self.param.get("linkelementid", "___Undefined____"))
        if linkbase is None:
            # search for fallback: all links with given class and all following link-elements
            fallback = self.soupcontent.find_all("a", {'class': self.param.get("linkfallbackclass", "___Undefined____")})
            links = self.get_sequence_of_element(fallback, "a")
            if len(links) == 0:
                # haven't found fallback links, use possible link
                return self.return_possible_link()
        else:
            links = linkbase.find_all("a")

        # add to self.possiblelinklist
        self.possiblelinklist_append(links)

        # return one good element of possiblelinklist
        return self.return_possible_link()

    def load_and_save_jokes(self):
        """Extract jokes from previously loaded soupcontent

        """
        if self.soupcontent is None:
            raise Exception("self.soupcontent is empty")

        hrwithoutclass = self.param.get("options", None) == "hrwithoutclass"

        # get main object
        mainelements = self.soupcontent.find_all(self.param.get("mainelement", "div"),
                                               {"class": self.param.get("mainelementclass", None)})

        stopelement = self.param.get("stopelement")


        # find hrs where jokes are stored until stopelement was found
        foundstopelement = False
        for me in mainelements:
            hrs = me.find_all("hr")

            for element in hrs:
                if hrwithoutclass and element.get('class', None) is not None:
                    continue

                text = ""

                # search until next hr element
                for nextel in element.next_elements:
                    if foundstopelement:
                        # do nothing, stop element was found
                        break

                    if isinstance(nextel, Tag) and nextel.name == "hr":
                        break
                    if isinstance(nextel, Tag) and nextel.name == "script":
                        continue
                    if isinstance(nextel, Tag) and nextel.name == stopelement:
                        foundstopelement = True
                        break

                    text += nextel.text

                author = None
                text = remove_unnecessary_spaces(text)
                if text == "":
                    # no joke found skip to next
                    continue

                # if we have to fetch author, find within last brackets
                if self.fetch_author:
                    textauthor = get_author_from_end(text, '~')
                    text = textauthor["text"]
                    author = textauthor["author"]

                joke = Joke(text, author)
                self.fun_db.save_joke_and_update_index(joke)




