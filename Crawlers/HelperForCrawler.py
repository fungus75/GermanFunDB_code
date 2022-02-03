"""
Helper-Functions for the crawlers
"""
import os
import shutil
from pathlib import Path


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

def get_author_from_top(text, begin_author_char, end_author_char):
    """extracts the author from the beginning of the string if it is sourrounded by begin_author_char and end_author_char

    :param text: the string that should be checked
    :param begin_author_char: the begin character for author
    :param end_author_char: (optional): the end character for author. If missing begin_author_char is taken
    :return: dictionary with "text" and "author" or None on error
    """

    # check/adjust parameters and set initial-values
    if text is None:
        return None

    author = None

    if end_author_char is not None:
        # try to find delimiter between author and text
        end_author_pos = text.find(end_author_char)
        if end_author_pos >= 0:
            # extract anything before end_author_char as author, rest as text
            author = remove_unnecessary_spaces(text[:end_author_pos - len(end_author_char) + 1])
            text = remove_unnecessary_spaces(text[end_author_pos + len(end_author_char):])

            # check if begin_author_char exists and text author starts with begin_author_char
            if begin_author_char is not None and begin_author_char == author[:len(begin_author_char)]:
                # yes, remove begin_author_char
                author = author[len(begin_author_char):]

    return {"text": text, "author": author}


def get_author_from_end(text, begin_author_char, end_author_char=None):
    """extracts the author from the end of a string if it is sourrounded by begin_author_char and end_author_char

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




