from __future__ import print_function
from future import standard_library
standard_library.install_aliases()

import unittest2 as unittest

import sys
if sys.version_info.major == 2:
    from mock import Mock, patch, PropertyMock
elif sys.version_info.major == 3:
    from unittest.mock import Mock, patch, PropertyMock

import numpy as np

from vsm import Corpus
import topicexplorer.prep

text = ['I', 'came', 'I', 'saw', 'I', 'conquered']
ctx_data = [np.array([(2, 'Veni'), (4, 'Vidi'), (6, 'Vici')],
                    dtype=[('idx', '<i8'), ('sentence_label', '|S6')])]

corpus = Corpus(text, context_data=ctx_data, context_types=['sentence'])

def test_get_corpus_counts():
    items, counts = topicexplorer.prep.get_corpus_counts(corpus)
    assert all(items == [0,1,2,3])
    assert all(counts == [3,1,1,1])

def test_get_small_words():
    assert topicexplorer.prep.get_small_words(corpus, 2) == ['I']
    assert topicexplorer.prep.get_small_words(corpus, 1) == []

def test_get_closest_bin():
    #assert topicexplorer.prep.get_closest_bin(corpus, 0) == 0 
    assert topicexplorer.prep.get_closest_bin(corpus, 0.2) == 1 
    assert topicexplorer.prep.get_closest_bin(corpus, 0.5) == 1 
    assert topicexplorer.prep.get_closest_bin(corpus, 0.7) == 3
    #assert topicexplorer.prep.get_closest_bin(corpus, 0, reverse=True) == 4
    assert topicexplorer.prep.get_closest_bin(corpus, 0.2, reverse=True) == 3 
    assert topicexplorer.prep.get_closest_bin(corpus, 0.5, reverse=True) == 3 
    assert topicexplorer.prep.get_closest_bin(corpus, 0.7, reverse=True) == 1