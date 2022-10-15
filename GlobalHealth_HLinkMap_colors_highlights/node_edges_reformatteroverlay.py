import json
import pickle5 as pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random


data = json.load(open('data.json','r'))
json.dump(data,open('data.json_bak','w'))

ghdbiomed= pickle.load(open('ListofGlobalHealthTokensOverlay.pickle','rb')) 

label_id = {}
id_label = {}
data = json.load(open('data.json','r'))

json.dump(data,open('data.json_bak','w'))
i = range(1,10)

for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'] in ghdbiomed:
        label_id[dictionary['label']] = dictionary['id']
        id_label[dictionary['id']] = dictionary['label']
        #color_ = dictionary['color'].split(',')
        #color_[1] = '255'
        #color = ",".join(color_)



#print(updatedcolors)
keys = list(id_label.keys())
for c,dictionary in enumerate(data['edges']):
    for i in range(len(keys)):
        if dictionary['source'] in keys[i]:
            print(True)
            #size_update = data['edges'][c]['size']*25
            data['edges'][c]['size'] = 10.0
            print(data['edges'][c]['size'])
        else:
            continue
for c,dictionary in enumerate(data['edges']):
    for i in range(len(keys)):
        if dictionary['target'] in keys[i]:
            #size_update = data['edges'][c]['size']*25
            data['edges'][c]['size'] = 10.0#size_update
        else:
            continue            
json.dump(data,open('data.json','w'))
