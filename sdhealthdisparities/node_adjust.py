# coding: utf-8
import os
import json
with open('data.json') as json_file:
    data = json.load(json_file)
for dictionaries in data['nodes']:
    if 'Research Cluster' in dictionaries['label']:
        size_ = {'size': 10.0 }
        dictionaries.update(size_)
json.dump(data,open('data.json','w'))
get_ipython().run_line_magic('save', "'node_adjust'  1-5") 
