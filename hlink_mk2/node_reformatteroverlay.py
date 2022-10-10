import json
import pickle5 as pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random


data = json.load(open('data.json','r'))
json.dump(data,open('data.json_bak','w'))

#ghdbiomed= pickle.load(open('ListofGlobalHealthTokensOverlay.pickle','rb')) 
hlink_tokens = pickle.load(open('/home/jimnoneill/HLINK_top_tokens.pickle','rb'))
label_id = {}
id_label = {}
data = json.load(open('data.json','r'))
colors  = (102,0,0)
json.dump(data,open('data.json_bak','w'))

for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'] in hlink_tokens:
        label_id[dictionary['label']] = dictionary['id']
        id_label[dictionary['id']] = dictionary['label']
        #color_ = dictionary['color'].split(',')
        #color_[1] = '255'
        #color = ",".join(color_)
        colorstr = str(colors)
        color_change = { 'color' : 'rgb'+colorstr }
        size_ = {'size': 1.0 }
        data['nodes'][c].update(size_)
        data['nodes'][c].update(color_change)
    elif dictionary['label'].startswith('HLINK'):
        colorstr = str(colors)
        color_change = { 'color' : 'rgb'+colorstr }
        size_ = {'size': 3.0 }
        data['nodes'][c].update(size_)
        data['nodes'][c].update(color_change)

sources  = []
for c,dictionary in enumerate(data['edges']):
    #print(c)
    #for i in range(len(keys)):
    s = dictionary['source']
    sources.append(s)

updatedcolors = {}
for i in sources:
    for key, values in idscolors.items():
        if i == key:
            updatedcolors[i] = idscolors.get(key)

#print(updatedcolors)
keys = list(updatedcolors.keys())
for c,dictionary in enumerate(data['edges']):
    for i in range(len(keys)):
        if dictionary['source'] in keys[i]:
            color_change = updatedcolors.get(keys[i])
            
            data['edges'][i].update(color_change)
            

json.dump(data,open('data.json','w'))
