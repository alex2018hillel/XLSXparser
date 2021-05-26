import json
from collections import Mapping

def find_catalogId(name_json):
    with open(name_json, "r") as read_file:
        data = json.load(read_file)
        del data['server']
        print("*"*60)
        contact = data['contact']
        contact.update({'email': 'automation+9614193@od.ab-soft.net'})
        contact.update({'contactPhone': '6502615189'})
        print(data)
        contact = str(contact)

        # print(general.keys())
        print("*"*60)


    def treeGet(d, name):
        if isinstance(d, Mapping):
            if name in d:
                yield d[name]
            for it in d.values():
                for found in treeGet(it, name):
                    yield found

    print(list(treeGet(data, 'catalogId')))
    return list(treeGet(data, 'catalogId'))

def add_info(name_json):
    with open(name_json, "r") as read_file:
        data = json.load(read_file)
        print("isAdmin - ", data['general']['isAdmin'])
        print("isLbo - ", data['general']['isLbo'])
        print("OFFERTYPE - ", data['general']['OFFERTYPE'])