import json
with open('usagov_bitly_data2012-03-16-1331923249.txt') as fd:
    records = [json.loads(line) for line in fd.readlines()]
#
# timezones = [rec ['tz'] for rec in records if 'tz' in rec]
# def get_counts(sequence):
#     counts = {}
#     for item in sequence:
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1
#     return counts
# res = get_counts(timezones)

# def top_counts(count_dict,n=10):
#     value_key_paris = [(count,tz) for tz,count in count_dict.items()]
#     value_key_paris.sort()
#     return value_key_paris[-n:]
# print(top_counts(res,n=4))
#
# from collections import Counter
# counts = Counter(timezones)
# print(counts.most_common(3))

from pandas import DataFrame
from pandas import Series
import pandas as pd
frame = DataFrame(records)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz==''] = 'Unknown'

# tz_counts = clean_tz.value_counts()
# results = Series([x.split()[0] for x in frame['a'].dropna()])
# print(results.value_counts())

print(frame[frame.a.notnull()])
