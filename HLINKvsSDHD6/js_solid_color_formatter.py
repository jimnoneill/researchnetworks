import json
import pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random
def flatten_once(xss):
    "Converts the list of lists into one list"
    return [x for xs in xss for x in xs]

data = json.load(open('data.json','r'))
json.dump(data,open('data.json_bak','w'))
data_meta,data_meta2,clusters,clusters2,tokens,tokens2,tokens_pmid,tokens_pmid2,overlay_matrices = pickle.load(open('/home/joneill/researchnetworks/HLINKvsSDHD6/data_meta,data_meta2,clusters,clusters2,tokens,tokens2,tokens_pmid,tokens_pmid2,overlay_matrices','rb'))
#hlink= pickle.load(open('hlinktokens.pickle','rb'))
hlink = list(set(flatten_once([list(set(flatten_once(l))) for l in tokens])))

label_id = {}
id_label = {}
data = json.load(open('data.json','r'))
colors  = (0,0,188)
json.dump(data,open('data.json_bak','w'))
i = range(1,10)

for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'] in hlink:
        label_id[dictionary['label']] = dictionary['id']
        id_label[dictionary['id']] = dictionary['label']

        colorstr = str(colors)
        color_change = { 'color' : 'rgb'+colorstr }
        size_ = {'size': 1.0 }
        data['nodes'][c].update(size_)
        data['nodes'][c].update(color_change)
    for i in range(10):
        if 'HLINK Projects Cluster ' + str(i+1)  in dictionary['label']:
            colorstr = str(colors)
            color_change = { 'color' : 'rgb'+colorstr }
            size_ = {'size': 3.0 }
            data['nodes'][c].update(size_)
            data['nodes'][c].update(color_change)


json.dump(data,open('data.json','w'))
