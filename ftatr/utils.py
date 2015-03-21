from collections import OrderedDict
import datetime


def build_index_by_name(items, attribute='name'):
    alphabet = OrderedDict()
    for letter in 'abcdefghijklmnopqrstuvwxyz#':
        alphabet[letter] = []
    for item in items:
        letter = item.__getattribute__(attribute).lower()[0]
        letter = letter if letter in 'abcdefghijklmnopqrstuvwxyz' else '#'
        alphabet[letter].append(item)
    return alphabet


def build_index_by_year(items, attribute='year'):
    timeline = OrderedDict()
    current_year = datetime.datetime.now().year
    first_year = items[0].__getattribute__(attribute)
    for year in reversed(range(first_year, current_year + 1)):
        timeline[year] = []
    for item in items:
        if item.year:
            timeline[item.year].append(item)
        else:
            if not '?' in timeline:
                timeline['?'] = []
            timeline['?'].append(item)

