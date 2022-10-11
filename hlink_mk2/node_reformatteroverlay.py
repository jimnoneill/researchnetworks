import json
import pickle5 as pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random


data = json.load(open('data.json','r'))
#json.dump(data,open('data.json_bak','w'))

#ghdbiomed= pickle.load(open('ListofGlobalHealthTokensOverlay.pickle','rb')) 
tokenslist = pickle.load(open('/home/jimnoneill/HLINK_top_tokens.pickle','rb'))

colors  = (102,0,0)
#json.dump(data,open('data.json_bak','w'))
idscolors = {}
for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'].startswith('HLINK'):
        #print(True)
        colorstr = str(colors)
        color_change = 'rgb'+colorstr
        size_ = {'size': 3.0 }
        data['nodes'][c]['size'] = 3.0
        data['nodes'][c]['color'] = color_change
        idscolors[idf] = color_change
    else:
        for i in range(len(tokenslist)):
            if dictionary['label'] in tokenslist[i]:
                idf = dictionary['id']
                colorstr = str(colors)
                color_change = 'rgb'+colorstr
                size_ = {'size': 1.0 }
                #idscolors[idf] = color_change
                data['nodes'][c]['size'] = 1.0
                data['nodes'][c]['color'] =color_change
                #print(color_change)



#keys = list(idscolors.keys())

#keys = list(idscolors.keys())
sources  = []
for c,dictionary in enumerate(data['edges']):
    #print(c)
    #for i in range(len(keys)):
    if sources in list(idscolors.keys()):
        s = dictionary['source']
        sources.append(s)

updatedcolors = {}
for i in sources:
    for key, values in idscolors.items():
        if i == key:
            updatedcolors[i] = idscolors.get(key)

#print(updatedcolors)
#keys = list(updatedcolors.keys())
for c,dictionary in enumerate(data['edges']):
    for i in range(len(sources)):
        if dictionary['source'] in sources:
            data['edges'][i]['color'] = color_change
            



json.dump(data,open('/home/jimnoneill/projects/NLP_topic_modeling/topicmodel_networks/researchnetworks/hlink_mk2/data.json','w'))
