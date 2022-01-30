import json
import os

class Joke:
    """Storing and converting one Joke

    This File is part of GermanFunDB, a German Fun Database for ML Projects
    """

    def __init__(
            self,
            joketext=None,
            author=None,
            postedtime=None,
            likes=None,
            import_filename=None,
    ):
        """Constructor.

        :param joketext: The joke text itself
        :param author: The author of the text, if known
        :param postedtime: the timepoint when the joke was posted
        :param likes: the number of likes
        :param import_filename: filename to load from
        """

        if joketext is None and import_filename is None:
            raise Exception("Please supply eater import_filename or joketext")

        if joketext is not None:
            # store into object and exit
            self.joketext = joketext
            self.author = author
            self.postedtime = postedtime
            self.likes = likes
            return

        if import_filename is not None:
            # load from file
            f = open(import_filename, "r")
            s = f.read()
            f.close()

            # convert to json
            data = json.loads(s)

            # fill as new data
            self.joketext = data.get('joketext')
            self.author = data.get('author', None)
            self.postedtime = data.get('postedtime', None)
            self.likes = data.get('likes', None)
            return

    def to_jsonstring(self):
        """returns the whole object as json-string

        :return: json-encoded string of the whole object
        """
        return json.dumps({
            "joketext": self.joketext,
            "author": self.author,
            "postedtime": self.postedtime,
            "likes": self.likes})

    def save_as_file(self, filename, overwrite=True):
        """saves the joke to a file

        :param filename: filename including path, as string
        :param overwrite: if true, existing file will e overwritten
        """

        if overwrite & os.path.exists(filename):
            os.remove(filename)     # remove file if exist and overwritte

        f = open(filename, "x")     # mode "x": if file exist (and was not deleted before), throw an error
        f.write(self.to_jsonstring())
        f.close()
