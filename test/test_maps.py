import collections
from nose.tools import istest, assert_equals

from ovation import Maps
from ovation.conversion import to_map, to_dict


@istest
def to_dict_should_convert_flat_map():
    m = Maps.newHashMap()
    m.put('key1', 'value1')
    m.put('key2', 2)

    d = to_dict(m)

    check_dict(d, m)


@istest
def to_map_should_convert_flat_dict():
    d = {'key1': 'value1',
         'key2': 2,
         3: 'value3',
         4: 5}

    m = to_map(d)

    check_dict(d, m)


def check_dict(d, m):
    for (k, v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)

        if isinstance(v, collections.Mapping):
            check_dict(v, m.get(k))
        else:
            if isinstance(v, basestring):
                actual = unicode(m.get(k))
                assert_equals(v, actual)
            elif isinstance(v, int):
                actual = m.get(k).intValue()
                assert_equals(v, actual)
            else:
                actual = m.get(k)
                assert v.equals(actual)


@istest
def to_map_should_convert_nested_dict():
    d = {'key1': 'value1',
         'nested': {'key2': 2,
                    3: 'value3',
                    4: 5}}

    m = to_map(d)

    check_dict(d, m)   
