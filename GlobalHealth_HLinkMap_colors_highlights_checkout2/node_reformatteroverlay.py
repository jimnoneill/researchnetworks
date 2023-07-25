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
colors  = (0,0,188)
json.dump(data,open('data.json_bak','w'))
i = range(1,10)

for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'] in ghdbiomed:
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
    for i in range(10):
        if 'Health Link Research Cluster ' + str(i+1)  in dictionary['label']:
            colorstr = str(colors)
            color_change = { 'color' : 'rgb'+colorstr }
            size_ = {'size': 3.0 }
            data['nodes'][c].update(size_)
            data['nodes'][c].update(color_change)


json.dump(data,open('data.json','w'))
