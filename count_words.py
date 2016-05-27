# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:28:58 2016

@author: n.davuluri
"""
import operator
import pdb
def count_words(s,n):
    word_count = dict()
    for word in s.split():
        if word_count.has_key(word):
            word_count[word] = word_count[word]+ 1
        else:
            word_count[word] = 1
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True) 
    top_n = sorted_word_count[0:n+1]

    return top_n
    
def test_run():
    """Test count_words() with some inputs."""
    
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
