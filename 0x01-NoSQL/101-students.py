#!/usr/bin/env python3
"""function: top_students"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    parse = list(mongo_collection.find())
    result = []
    for line in parse:
        av = 0
        inner = {}
        inner['_id'] = line['_id']
        inner['name'] = line['name']
        for sco in line['topics']:
            av += sco['score']
        inner['averageScore'] = av / len(line['topics'])
        result.append(inner)
    sorted_r = sorted(result, key=lambda x: x['averageScore'], reverse=True)
    return list(sorted_r)
