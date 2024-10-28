#!/usr/bin/env python3
'''
    Script function to take two argument.
'''


def index_range(page, page_size):
    '''
        Returns the range of indexes for a given page.
    '''
    page_start = (page - 1) * page_size
    page_end = page * page_size
    return page_start, page_end
