import json
import pickle5 as pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random


ghdbiomed= pickle.load(open('GlobalHealth726.pickle','rb'))
#colors = [(128,0,0),(165,42,42),(255,0,0),(255,215,0),(238,232,170),(255,255,0),(154,205,50),(127,255,0),(0,128,0),(143,188,143),(102,205,170),(47,79,79),(0,128,128),(0,255,255),(224,255,255),(64,224,208),(127,255,212),(70,130,180),(100,149,237),(0,191,255),(30,144,255),(135,206,250),(0,0,128),(0,0,255),(138,43,226),(75,0,130),(123,104,238),(139,0,139),(148,0,211),(186,85,211),(221,160,221),(238,130,238),(255,0,255),(199,21,133),(255,20,147),(255,192,203),(255,228,196),(139,69,19),(244,164,96),(188,143,143),(255,240,245),(245,255,250),(112,128,144),(240,255,240)]
colors = pickle.load(open('RGBColors.pickle','rb'))

random.shuffle(colors)

tokenslist = []
for i in range(len(ghdbiomed)):
    tokens = []
    for j in ghdbiomed[i]:
        tokens.append(j)
    tokenslist.append(tokens)

data = json.load(open('data.json','r'))
json.dump(data,open('data.json_bak','w'))

idscolors = {} 
for c,dictionary in enumerate(data['nodes']):
    for i in range(len(tokenslist)):
        if dictionary['label'] in tokenslist[i]:
            idf = dictionary['id']
            colorstr = str(colors[i])
            color_change = { 'color' : 'rgb'+colorstr }
            size_ = {'size': 1.0 }
            idscolors[idf] = color_change
            data['nodes'][c].update(size_)
            data['nodes'][c].update(color_change)
            #print(color_change)
        elif 'Global Health Disparity Research Cluster ' + str(i+1)  in dictionary['label']:
            colorstr = str(colors[i])
            color_change = { 'color' : 'rgb'+colorstr }
            size_ = {'size': 3.0 }
            data['nodes'][c].update(size_)
            data['nodes'][c].update(color_change)


keys = list(idscolors.keys())

for c,dictionary in enumerate(data['edges']):
    for i in range(len(keys)):
        if dictionary['id'] in keys[i]:
            color_change = idscolors.get(keys[i])
            #print(color_change)
            data['edges'][c].update(color_change)

ghdbiomed= pickle.load(open('ListofSDTokensOverlay.pickle','rb')) 
label_id = {}
id_label = {}
data = json.load(open('data.json','r'))
json.dump(data,open('data.json_bak','w'))
for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'] in ghdbiomed:
        label_id[dictionary['label']] = dictionary['id']
        id_label[dictionary['id']] = dictionary['label']
        color_ = dictionary['color'].split(',')
        color_[1] = '255'
        color = ",".join(color_)
        color_change = { 'color' : str(color) }
        data['nodes'][c].update(color_change)
for c,dictionary in enumerate(data['edges']):
    if dictionary['source'] in list(id_label.keys()) and dictionary['target'] in list(id_label.keys()):
        print(True)
        color_ = dictionary['color'].split(',')
        color_[1] = '255'
        color = ",".join(color_)
        color_change = { 'color' : str(color) }
        data['edges'][c].update(color_change)
    elif dictionary['source'] in list(id_label.keys()) or dictionary['target'] in list(id_label.keys()):
        color_ = dictionary['color'].split(',')
        color_change = str(int(np.mean([255,int(color_[1])])))
        color_[1] = color_change
        color = ",".join(color_)
        color_change = { 'color' : str(color) }
        data['edges'][c].update(color_change)


json.dump(data,open('data.json','w'))
