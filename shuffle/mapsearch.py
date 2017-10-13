"""
Created on Oct 12th.

author: tzhang
"""

import pandas as pd
from pytrends.request import TrendReq
from collections import deque
import nltk
from nltk.stem.snowball import SnowballStemmer
import random


STEMMER = SnowballStemmer('english')


def search_generate(seed_keyword, top=True):
    pytrends = TrendReq()
    pytrends.build_payload([seed_keyword])
    if top:
        return pytrends.related_queries()[seed_keyword]['top']['query'].tolist()
    else:
        return pytrends.related_queries()[seed_keyword]['rising']['query'].tolist()


def get_related_keywords(seed_keyword):
    """

    :param seed_keyword: str, seed keyword
    :return: list, a list of the related keywords of the seed keyword
    """
    result = []
    seed_keyword_stem_set = set(STEMMER.stem(part) for part in nltk.word_tokenize(seed_keyword))
    for related_keyword in search_generate(seed_keyword):
        related_keyword_stem = [STEMMER.stem(part) for part in nltk.word_tokenize(related_keyword)]
        exclude = any(p in seed_keyword_stem_set for p in related_keyword_stem)
        if not exclude:
            result.append(related_keyword)
    return result


def expand(seed_keyword, depth=3):
    """
    Basically do a BFS

    :param seed_keyword: seed keyword to start the expansion
    :param depth:
    :return:
    """
    # pytrends = TrendReq(hl='en-US', tz=360)
    candidate_keywords = deque([seed_keyword])
    level = 0
    while level < depth:
        cur_size = len(candidate_keywords)
        for i in range(cur_size):
            related_kwgs = get_related_keywords(candidate_keywords.popleft())
            for kwg in related_kwgs:
                candidate_keywords.append(kwg)
        level += 1
    return list(candidate_keywords)

# pytrends = TrendReq(hl='en-US', tz=360)
print search_generate('smartphone')
# expanded_kwgs = expand('smartphone', depth=1)
# print len(expanded_kwgs)
# print expanded_kwgs