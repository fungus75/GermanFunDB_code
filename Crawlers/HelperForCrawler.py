"""
Helper-Functions for the crawlers
"""
import os
import shutil
from pathlib import Path


def get_next_index_from_file(filename):
    """loads and increases an integer index from a indexfile

    :param filename: the index-file
    """

    # start with 0 as index
    next_index = 0

    # if file was found, load content and increase by one
    if os.path.exists(filename):
        last_index = int(get_file_as_string(filename))
        next_index = last_index + 1

    # update index file and return new index
    f = open(filename, "w")
    f.write(str(next_index))
    f.close()

    return next_index


def save_joke_and_update_index(joke, jokedir):
    """saves joke and updates index

    :param joke: the joke to be saves
    :param jokedir: the folder where to store jokes and index-file
    """

    # get next index and save joke as file
    next_index = get_next_index_from_file(jokedir + "/jokeidx")
    joke.save_as_file(jokedir + "/joke_" + str(next_index))


def get_full_url(urlpart, url_base):
    """gets a working url from a possible url-part compairedto compair_base

    :param urlpart: the (possible) part of an url
    :param url_base: the url-base where the urlpart is relativly to or None on error
    """

    if urlpart is None:
        return urlpart

    # if url starts with http or https, all is good
    if urlpart[:5] == "http:" or urlpart[:6] == "https:":
        return urlpart

    # if url starts with / we have to extract servername
    # since url is always in format http://servername/ or https://servername/,
    # we have to find 3rd slash
    if urlpart[0] == "/":
        end_of_servername = get_indexed_element_from_string(url_base,"/", 3)
        if end_of_servername == -1:
            return None
        return url_base[:end_of_servername] + urlpart

    # last try: concat urlpart at the end of url_base but split filename from urlbase in advance
    lastslash = url_base.rfind("/")
    url_base_without_file = url_base
    if lastslash >= 0:
        url_base_without_file = url_base[:lastslash]
    return url_base_without_file + "/" + urlpart

def get_file_as_string(filename):
    """gets a full file as one string

    :param filename: filename
    :return: the content as one big string
    """
    f = open(filename, "r")
    string = f.read()
    f.close()
    return string


def get_indexed_element_from_string(string, substring, index):
    """gets the indexed element out of a string,
    e.g. if string = http://server/, substring = / and index = 3, the position of the 3rd slash would be returned

    :param string: the string where to search
    :param substring: the substring to search for
    :param index: the number of element to find (see example)
    :return -1 if nothing was found, else the position of the searched substring
    """

    if string is None:
        return None

    # start at the beginning
    start = 0
    find_pos = -1
    for i in range(index):
        find_pos = string.find(substring, start)
        if find_pos < 0:
            # we didn't find it, return -1
            return -1

        # start searching again after the last found position
        start = find_pos + 1

    return find_pos


def convert_workdir_to_json(export_file, workdir):
    """converts the given workdir into a export-file in json-format

    :param export_file the json-file where all data should be saved
    :param workdir the workdir from generation step
    """

    # check total number of websites
    total_websites = int(get_file_as_string(workdir + "/webidx")) + 1

    # open outputfile and prepare JSON-Beginning
    jsonfile = open(export_file, "w")
    jsonfile.write('[');
    overall_jokes_amount = 0

    # process each webfolder
    for webidx in range(total_websites):
        webdir = workdir + "/web_" + str(webidx)
        print("Processing " + webdir)

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


def get_author_from_end(text, begin_author_char, end_author_char=None):
    """etracts the author from the end of a string if it is sourrounded by begin_author_char and end_author_char

    :param text: the string that should be checked
    :param begin_author_char: the begin character for author
    :param end_author_char: (optional): the end character for author. If missing begin_author_char is taken
    :return: dictionary with "text" and "author" or None on error
    """

    # check/adjust parameters and set initial-values
    if text is None:
        return None
    if end_author_char is None:
        end_author_char = begin_author_char
    author = None

    # if we have a begin_author_char
    if begin_author_char is not None:
        # search last begin_author_char
        lastbracket = text.rfind(begin_author_char)
        if lastbracket >= 0:
            # all after is author
            author = text[lastbracket + len(begin_author_char):].strip()
            # if author ends with end_author_char => split it away
            if author[-len(end_author_char)] == end_author_char:
                author = author[:len(author) - len(end_author_char)]

            # remaining text is until begin_author_char
            text = text[:lastbracket - len(begin_author_char)].strip()

    return {"text": text, "author": author}


def remove_unnecessary_spaces(text):
    """removes unnecessary spaces within text (comparable to strip

    :param text: the text
    :return: cleaned text
    """

    text = text.strip().replace('\n', ' ').replace('\r', '')
    while text.find('  ')>=0:
        text = text.replace('  ', ' ')

    return text.strip()


def import_into_workdir(importdir, workdir):
    """Imports (Merges) another workdir into the current workdir

    :param importdir: the workdir-folder of another jokedb to be imported into given workdir
    :param workdir: workdir of current fundb
    """

    if not os.path.exists(importdir) or not os.path.exists(importdir + "/webidx"):
        # nothing to do, importdir do not exist or is no jokedb
        return

    if importdir == workdir:
        # can not import db itself into db
        return

    # create workdir if not exist
    path = Path(workdir)
    path.mkdir(parents=True, exist_ok=True)

    # start importing
    total_websites = int(get_file_as_string(importdir + "/webidx")) + 1

    # process each webfolder
    for webidx in range(total_websites):
        webdir = importdir + "/web_" + str(webidx)

        newidx = get_next_index_from_file(workdir + "/webidx")
        newwebdir = workdir + "/web_" + str(newidx)

        print("Importing Processing " + webdir + " as " +  newwebdir)
        shutil.copytree(webdir, newwebdir)


