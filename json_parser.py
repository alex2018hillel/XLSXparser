import itertools
import json
from collections import Mapping
from find_in_string import find_number_test

def full_data(name_json, string):
    with open(name_json, "r") as read_file:
        data = json.load(read_file)
        del data['server']
        contact = data['contact']
        contact.update({'email': 'automation+9614193@od.ab-soft.net'})
        contact.update({'contactPhone': '6502615189'})
        full_data = 'CookieCNVR' + find_number_test(string) + ',"' + str(data).replace(': ', ':').replace(', ', ',') + '"'
        return full_data

def find_catalogId(name_json):
    with open(name_json, "r") as read_file:
        data = json.load(read_file)
        del data['server']
        contact = data['contact']
        contact.update({'email': 'automation+9614193@od.ab-soft.net'})
        contact.update({'contactPhone': '6502615189'})

    def treeGet(d, name):
        if isinstance(d, Mapping):
            if name in d:
                yield d[name]
            for it in d.values():
                for found in treeGet(it, name):
                    yield found

    catalogId_list = list(treeGet(data, 'catalogId'))
    # for j in reversed(catalogId_list):
    #     pass
    qty_list = list(treeGet(data, 'qty'))
    data_list = []
    for i in itertools.zip_longest(reversed(catalogId_list), reversed(qty_list),  fillvalue=0):
        data_list.append(i)
    return [data_list]

def add_info(name_json):
    with open(name_json, "r") as read_file:
        data = json.load(read_file)
        print("planDuration - ", data['general']['planDuration'])
        print("isAdmin - ", data['general']['isAdmin'])
        print("isLbo - ", data['general']['isLbo'])
        print("OFFERTYPE - ", data['general']['OFFERTYPE'])