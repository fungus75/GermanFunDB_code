#
# Exports existing DB into different formats
#

from Crawlers.CrawlerFactory import CrawlerFactory

from FunDB.FunDB import FunDB

import configuration as cfg

fun_db = FunDB(cfg.WORKDIR)

# creating output
fun_db.export_json(cfg.EXPORTJSON)
fun_db.export_csv(cfg.EXPORTCSVSOURCES, cfg.EXPORTCSVDATA)



