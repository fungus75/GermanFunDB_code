from Crawlers.CrawlerDeutschlernen import CrawlerDeutschlernen
from Crawlers.CrawlerJusthr import CrawlerJusthr
from Crawlers.CrawlerJustli import CrawlerJustli
from Crawlers.CrawlerSmsat import CrawlerSmsat
from Crawlers.CrawlerWitzeat import CrawlerWitzeat
from Crawlers.CrawlerWitzenet import CrawlerWitzenet
from Crawlers.CrawlerTranslateFUNDataset import CrawlerTranslateFUNDataset
from Crawlers.CrawlerTranslaterJokesData import CrawlerTranslaterJokesData
from Crawlers.FileImporter.csvImport import CrawlerCSVImport


class CrawlerFactory:
    """Factory class for creating new crawlers

    """

    @staticmethod
    def get_crawler(fun_db, param):
        """gets (creates) a new crawler class

        :param fun_db: initialilzed fun_db for storing information
        :param param: dictinary with at least the following elements: "url", "type" and "crawler"
        :return: new crawler-instance
        """

        # check if critical params are missing
        if param is None or param.get("url", None) is None or param.get("type", None) is None or param.get("crawler", None) is None:
            raise Exception("Param does not exist or missing params")

        # list of possible crawlers and their classes
        possible_crawlers = {
            "smsat": CrawlerSmsat,
            "deutschlernen": CrawlerDeutschlernen,
            "witzenet": CrawlerWitzenet,
            "justli": CrawlerJustli,
            "justhr": CrawlerJusthr,
            "witzeat": CrawlerWitzeat,
            "translate_fundataset": CrawlerTranslateFUNDataset,
            "translate_rjokesdata": CrawlerTranslaterJokesData,
            "csvimport": CrawlerCSVImport,

        }

        # get crawler-class
        crawler = possible_crawlers.get(param.get("crawler"), None)
        if crawler is None:
            raise Exception("Non-Existing crawler requested: " + param.get("crawler"))

        # return newly created crawler-instance
        return crawler(fun_db, param)

