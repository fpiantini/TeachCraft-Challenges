from __future__ import absolute_import
import collections
import six
from six.moves import map

def flatten(l):
    for e in l:
        if isinstance(e, collections.Iterable) and not isinstance(e, six.string_types):
            for ee in flatten(e): yield ee
        else: yield e

def flatten_parameters_to_string(l):
    return ",".join(map(str, flatten(l)))
