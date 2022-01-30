from Crawlers.CrawlerSmsat import CrawlerSmsat


class CrawlerFactory:
    """Factory class for creating new crawlers

    """

    @staticmethod
    def get_crawler(param):
        """gets (creates) a new crawler class

        :param param: dictinary with at least the following elements: "url", "type" and "crawler"
        :return: new crawler-instance
        """

        # check if critical params are missing
        if param is None or param.get("url", None) is None or param.get("type", None) is None or param.get("crawler", None) is None:
            raise Exception("Param does not exist or missing params")

        # list of possible crawlers and their classes
        possible_crawlers = {
            "smsat": CrawlerSmsat,
        }

        # get crawler-class
        crawler = possible_crawlers.get(param.get("crawler"), None)
        if crawler is None:
            raise Exception("Non-Existing crawler requested: " + param.get("crawler"))

        # return newly created crawler-instance
        return crawler(param)

