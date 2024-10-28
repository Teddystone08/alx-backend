#!/usr/bin/env python3
"""Script that takes two argument"""

def index_range(page, page_size):
    '''
    Return page index in a given range

    '''
    page_start = (page -1) * page_size
    page_end = page_start + page_size
    return page_start, page_end
