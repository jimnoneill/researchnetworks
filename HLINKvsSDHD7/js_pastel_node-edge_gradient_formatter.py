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
data_meta,data_meta2,clusters,clusters2,tokens,tokens2,tokens_pmid,tokens_pmid2,overlay_matrices = pickle.load(open('/home/joneill/researchnetworks/HLINKvsSDHD7/data_meta,data_meta2,clusters,clusters2,tokens,tokens2,tokens_pmid,tokens_pmid2,overlay_matrices','rb'))
#hlink= pickle.load(open('hlinktokens.pickle','rb'))
tokenslist = [list(set(flatten_once(l))) for l in tokens2]
ghdbiomed = tokenslist
#ghdbiomed= pickle.load(open('GHTokens.pickle','rb'))
#colors = [(128,0,0),(165,42,42),(255,0,0),(255,215,0),(238,232,170),(255,255,0),(154,205,50),(127,255,0),(0,128,0),(143,188,143),(102,205,170),(47,79,79),(0,128,128),(0,255,255),(224,255,255),(64,224,208),(127,255,212),(70,130,180),(100,149,237),(0,191,255),(30,144,255),(135,206,250),(0,0,128),(0,0,255),(138,43,226),(75,0,130),(123,104,238),(139,0,139),(148,0,211),(186,85,211),(221,160,221),(238,130,238),(255,0,255),(199,21,133),(255,20,147),(255,192,203),(255,228,196),(139,69,19),(244,164,96),(188,143,143),(255,240,245),(245,255,250),(112,128,144),(240,255,240)]
colors = pickle.load(open('pastel_colors.pickle','rb'))

random.shuffle(colors)

tokenslist = []
for i in range(len(ghdbiomed)):
    tokens = []
    for j in ghdbiomed[i]:
        tokens.append(j)
    tokenslist.append(tokens)

data = json.load(open('data.json','r'))
json.dump(data,open('data.json_bak2','w'))

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
        elif 'SDHD Research Cluster ' + str(i+1)  in dictionary['label']:
            idf = dictionary['id']
            colorstr = str(colors[i])
            color_change = { 'color' : 'rgb'+colorstr }
            size_ = {'size': 3.0 }
            idscolors[idf] = color_change
            data['nodes'][c].update(size_)
            data['nodes'][c].update(color_change)

sources  = []
for c,dictionary in enumerate(data['edges']):
    s = dictionary['source']
    sources.append(s)

updatedcolors = {}
for i in sources:
    for key, values in idscolors.items():
        if i == key:
            updatedcolors[i] = idscolors.get(key)

keys = list(updatedcolors.keys())
for c,dictionary in enumerate(data['edges']):
    for i in range(len(keys)):
        if dictionary['source'] in keys[i]:
            color_change = updatedcolors.get(keys[i])
            data['edges'][i].update(color_change)
            

json.dump(data,open('data.json','w'))
