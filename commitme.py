# -*- coding: utf-8 -*-
"""
"""


__author__ = 'Ben Lopatin'
__email__ = 'ben@wellfire.co'
__version__ = '0.1.0'

import functools


def save(commit):
    """
    """
    def wrapper(func):
        @functools.wraps(func)
        def decorator(obj, *args, **kwargs):
            do_commit = kwargs.pop('commit', commit)
            func(obj, *args, **kwargs)
            if do_commit:
                obj.save()
            # introspect func's defined kwargs to look for a commit?
        return decorator
    return wrapper
