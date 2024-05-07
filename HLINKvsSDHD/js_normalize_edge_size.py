import json
import pickle5 as pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random


data = json.load(open('data.json','r'))
json.dump(data,open('data.json_bak','w'))

hlink= pickle.load(open('hlinktokens.pickle','rb'))

label_id = {}
id_label = {}
data = json.load(open('data.json','r'))

json.dump(data,open('data.json_bak','w'))
i = range(len(hlink)
for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'] in hlink:
        label_id[dictionary['label']] = dictionary['id']
        id_label[dictionary['id']] = dictionary['label']

    for i in range(10):
        if 'HLINK ' + str(i+1)  in dictionary['label']:
            label_id[dictionary['label']] = dictionary['id']
            id_label[dictionary['id']] = dictionary['label']


keys = list(id_label.keys())
for c,dictionary in enumerate(data['edges']):
    if dictionary['source'] in keys:
        print(True)
        data['edges'][c]['size'] = 10.0
        print(data['edges'][c]['size'])
    else:
        continue

json.dump(data,open('data.json','w'))
