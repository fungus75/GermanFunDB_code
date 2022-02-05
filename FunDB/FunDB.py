import json
import os
import shutil
import csv
from pathlib import Path

from Crawlers.HelperForCrawler import get_file_as_string


class FunDB():
    """Class for Management of a FunDB, created for storage of the GermanFUNDB

    """

    def __init__(
            self,
            basedir
    ):
        """Constructor

        :param basedir: Base Directory for storage of the funDB
        """

        # read params and create basedir
        self.jokesdir = None
        self.fullwebworkdir = None
        self.basedir = basedir
        path = Path(self.basedir)
        path.mkdir(parents=True, exist_ok=True)



    def get_next_index_from_file(self, filename):
        """loads and increases an integer index from a indexfile

        :param filename: the index-file, relative to basedir
        """

        # start with 0 as index
        next_index = 0

        # if file was found, load content and increase by one
        if os.path.exists(self.basedir + "/" + filename):
            last_index = int(get_file_as_string(self.basedir + "/" + filename))
            next_index = last_index + 1

        # update index file and return new index
        f = open(self.basedir + "/" + filename, "w")
        f.write(str(next_index))
        f.close()

        return next_index

    def switch_jokedir(self, jokedir):
        """Switches the current jokedir to the given jokedir relative to self.basedir

        :param jokedir: new jokedir, relative to self.basedir
        """

        # prepare workfolder for current task
        self.fullwebworkdir = self.basedir + "/" + jokedir
        self.jokesdir = jokedir + "/jokes"
        self.fulljokesdir = self.basedir + "/" + self.jokesdir
        if not os.path.exists(self.fullwebworkdir):
            os.mkdir(self.fullwebworkdir)

        if not os.path.exists(self.fulljokesdir):
            os.mkdir(self.fulljokesdir)

    def write_info(self, info):
        if self.fullwebworkdir is None:
            raise Exception("jokedir must be set before by using switch_jokedir")

        infofile = open(self.fullwebworkdir + "/info", "w")
        infofile.write(json.dumps(info))
        infofile.close()



    def save_joke_and_update_index(self, joke):
        """saves joke and updates index

        :param joke: the joke to be saves
        """

        # get next index and save joke as file
        next_index = self.get_next_index_from_file(self.jokesdir + "/jokeidx")
        joke.save_as_file(self.fulljokesdir + "/joke_" + str(next_index))

    def export_json(self, export_file):
        """converts the whole database into an export-file in json-format

        :param export_file the json-file where all data should be saved
        :param workdir the workdir from generation step
        """

        # check total number of websites
        total_websites = int(get_file_as_string(self.basedir + "/webidx")) + 1

        # open outputfile and prepare JSON-Beginning
        jsonfile = open(export_file, "w")
        jsonfile.write('[');
        overall_jokes_amount = 0

        # process each webfolder
        for webidx in range(total_websites):
            webdir = self.basedir + "/web_" + str(webidx)
            print("JSON-Processing " + webdir)

            if webidx > 0:
                jsonfile.write(',\n')

            # copy info into json
            info = get_file_as_string(webdir + "/info")
            jsonfile.write('{"info": ' + info + ',\n')

            # load jokes
            total_jokes = int(get_file_as_string(webdir + '/jokes/jokeidx')) + 1
            overall_jokes_amount += total_jokes
            print("  Jokes: " + str(total_jokes))
            jsonfile.write(' "jokes": [')
            for jokeidx in range(total_jokes):
                joke = get_file_as_string(webdir + '/jokes/joke_' + str(jokeidx))
                if jokeidx > 0:
                    jsonfile.write(',\n  ')
                jsonfile.write(joke)
            jsonfile.write(']}')

        # close file and json ending
        jsonfile.write(']')
        jsonfile.close()
        print("Overall joke amount: " + str(overall_jokes_amount))

    def export_csv(self, source_filename, data_filename):
        """exports the whole database into 2 export files: one with all the source-infos (links, queried at,...)
           and one with the data itself

        :param source_filename: full path for the source-info-file
        :param data_filename: full path for the data-file
        """

        # open both files and write header
        srcfile = open(source_filename, "w")
        srcwriter = csv.writer(srcfile, dialect="unix")
        srcwriter.writerow(["id", "url", "type", "crawler", "timestamp"])

        datafile = open(data_filename, "w")
        datawriter = csv.writer(datafile, dialect="unix")
        datawriter.writerow(["id", "src", "joketext", "author", "postedtime", "likes"])

        overall_jokes_idx = 0

        # check total number of websites and process each webfolder
        total_websites = int(get_file_as_string(self.basedir + "/webidx")) + 1
        for webidx in range(total_websites):
            webdir = self.basedir + "/web_" + str(webidx)
            print("CSV-Processing " + webdir)

            # read src ("info")
            src = json.loads(get_file_as_string(webdir + "/info"))

            # reformat to csv and write into csv-file
            # srcwriter.writerow(["id", "url", "type", "crawler", "timestamp"])
            param = src.get("param")
            srcrow = [webidx, param.get("url"),
                      param.get("type"),
                      param.get("crawler"),
                      src.get("timestamp")]
            srcwriter.writerow(srcrow)

            # load jokes
            total_jokes = int(get_file_as_string(webdir + '/jokes/jokeidx')) + 1
            print("  overall_jokes_idx: " + str(overall_jokes_idx))
            for jokeidx in range(total_jokes):
                joke = json.loads(get_file_as_string(webdir + '/jokes/joke_' + str(jokeidx)))

                # reformat to csv and write into csv-file
                # datawriter.writerow(["id", "src", "joketext", "author", "postedtime", "likes"])
                overall_jokes_idx += 1
                datarow = [overall_jokes_idx, webidx,
                           joke.get("joketext"),
                           joke.get("author"),
                           joke.get("postedtime"),
                           joke.get("likes")]
                datawriter.writerow(datarow)

        # close files and finish
        srcfile.close()
        datafile.close()

    def import_workdir(self, importdir):
        """Imports (Merges) another workdir into the current workdir

        :param importdir: the workdir-folder of another jokedb to be imported into given workdir
        :param workdir: workdir of current fundb
        """

        if not os.path.exists(importdir) or not os.path.exists(importdir + "/webidx"):
            # nothing to do, importdir do not exist or is no jokedb
            return

        if importdir == self.basedir:
            # can not import db itself into db
            return

        # create workdir if not exist
        path = Path(self.basedir)
        path.mkdir(parents=True, exist_ok=True)

        # start importing
        total_websites = int(get_file_as_string(importdir + "/webidx")) + 1

        # process each webfolder
        for webidx in range(total_websites):
            webdir = importdir + "/web_" + str(webidx)

            newidx = self.get_next_index_from_file("/webidx")
            newwebdir = self.basedir + "/web_" + str(newidx)

            print("Importing Processing " + webdir + " as " + newwebdir)
            shutil.copytree(webdir, newwebdir)


