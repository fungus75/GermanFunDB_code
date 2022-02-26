import hashlib
import os
import requests

# the Google Translate API Endpoint. Leave it, should work
TRANSLATEAPIENDPOINT = 'https://translation.googleapis.com/language/translate/v2'

# Chaching
googleTranslateCache = {}


def simpleGoogleTranslate(text, srcLan, dstLan):
    """simple google translation API call
    Can be used to translate the given text from "srcLan" (ISO-Code of source Language, i.E. "de" for german)
    to dstLan (ISO-Code of destination Language)

    to save API-calls this function uses a basic caching routine

    Attention: to get this working, you have to set GOOGLEAPIKEY environment variable

    If there is an error, this method returns None

    :param text: Text to be translated
    :param srcLan: source-language (current language of text)
    :param dstLan: destination language
    :return: translated text or None on error
    """
    if srcLan == dstLan:
        # translate from same language to same langage ==> do nothing, just return given text
        return text

    # check if text is useful (i.E. not empty and not None)
    if text is None:
        return None

    # remove unnecessary whitespaces in front of or at end of text
    text = text.strip()
    if text == "":
        return None

    # calculate key for cache
    key = hashlib.md5(str(str(srcLan) + ":" + dstLan + ":" + text).encode("utf-8")).hexdigest()

    # check cache
    cacheValue = googleTranslateCache.get(key, None)
    if cacheValue is not None:
        # Cache hit, return value and exit
        return cacheValue

    # cache miss, printout cache miss and call google api
    # print("Cache miss")

    # fill data as required form google-translate-rest-api-call
    data = {'q': text, 'source': srcLan, 'target': dstLan, 'format': 'text'}

    # call api
    r = requests.post(TRANSLATEAPIENDPOINT + '?key=' + os.environ['GOOGLEAPIKEY'], json=data)

    # parse result and check if result was ok
    result = r.json()
    if result['data'] and result['data']['translations'] and result['data']['translations'][0] and result['data']['translations'][0]['translatedText']:
        translatedValue = result['data']['translations'][0]['translatedText']
        googleTranslateCache[key] = translatedValue
        return translatedValue

    # no good result returned from api
    return None


