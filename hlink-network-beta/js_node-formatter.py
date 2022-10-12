import json
import pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random
import os 
### new plan, 10/11/22 - load top tokens relative to groups. enumerate over groups to align them with node color changes. 
hlink_tokens = pickle.load(open('/home/jimnoneill/HLINK_top_tokens.pickle','rb'))

group_top_sd_tokens,group_top_hd_tokens = pickle.load(open('/home/jimnoneill/group_top_sd_tokens,group_top_hd_tokens.pickle','rb'))
ghd_tokens = pickle.load(open('/home/jimnoneill/ghd_top_tokens.pickle','rb'))
overlap_tokens = list(set(ghd_tokens).intersection(set(hlink_tokens)))
colors = pickle.load(open('/home/jimnoneill/rgb_colors_large.pickle','rb'))
random.shuffle(colors)

tokenslist = ghd_tokens##[]
#for i in range(len(ghdbiomed)):
    #tokens = []
    #for j in ghdbiomed[i]:
        #tokens.append(j)
    #tokenslist.append(tokens)

data = json.load(open('data.json','r'))
if os.path.exists('data.json_bak') is False:
    json.dump(data,open('data.json_bak','w'))
color_index = 0
idscolors = {} 
cluster_colors = {}
for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'].startswith('Global Health'):
        cluster = int(dictionary['label'][-2:].strip())
        #print(dictionary)
        idf = dictionary['id']
        colorstr = str(colors[color_index])
        color_change = 'rgb'+colorstr
        #print(type(color_change))
        size_ = {'size': 3.0 }
        idscolors[idf] = color_change
        data['nodes'][c]['size'] = 3.0
        data['nodes'][c]['color'] = color_change
        cluster_colors[cluster] = color_change
        color_index += 1

    else:
        continue
for n,group in enumerate(group_top_hd_tokens):
    n +=1
    color_change = cluster_colors[n]
    for c,dictionary in enumerate(data['nodes']):
        if dictionary['label'] in group:
            #print(dictionary)
            idf = dictionary['id']
            #colorstr = str(colors[color_index])
            #color_change = 'rgb'+colorstr
            #print(type(color_change))
            size_ = {'size': 1.0 }
            idscolors[idf] = color_change
            data['nodes'][c]['size'] = 1.0
            data['nodes'][c]['color'] = color_change
            #color_index += 1

        else:
            continue

for c,dictionary in enumerate(data['edges']):
    for ids,colors in idscolors.items():
        if dictionary['source'] == ids:
            data['edges'][c]['color'] = colors
            
            

#color_index = 0
idscolors = {} 
cluster_colors = {}
for c,dictionary in enumerate(data['nodes']):
    if dictionary['label'].startswith('HLINK'):
        cluster = int(dictionary['label'][-2:].strip())
        #print(dictionary)
        idf = dictionary['id']
        colorstr = '(102,0,0)'#str(colors[color_index])
        color_change = 'rgb'+colorstr
        #print(type(color_change))
        size_ = {'size': 3.0 }
        idscolors[idf] = color_change
        data['nodes'][c]['size'] = 3.0
        data['nodes'][c]['color'] = color_change
        cluster_colors[cluster] = color_change
        #color_index += 1

    else:
        continue



for n,group in enumerate(group_top_sd_tokens):
    n +=1
    try:
        color_change = cluster_colors[n]
        for c,dictionary in enumerate(data['nodes']):
            if dictionary['label'] in group:
                #print(dictionary)
                idf = dictionary['id']
                #colorstr = str(colors[color_index])
                #color_change = 'rgb'+colorstr
                #print(type(color_change))
                data['nodes'][c]['size'] = 1.0

                idscolors[idf] = color_change
                
                data['nodes'][c]['color'] = color_change
                
                if dictionary['label'] in overlap_tokens:
                    og_color = data['nodes'][c]['color']
                    og_color = og_color.replace('rgb(','').split(',')
                    og_color[0] == 'rgb(102'
                    new_color = ','.join(og_color)
                    data['nodes'][c]['color'] = new_color
            #color_index += 1

            else:
                continue
    except KeyError:
        continue

for c,dictionary in enumerate(data['edges']):
    for ids,colors in idscolors.items():
        if dictionary['source'] == ids:
            data['edges'][c]['color'] = colors
            
            






json.dump(data,open('/home/jimnoneill/projects/NLP_topic_modeling/topicmodel_networks/researchnetworks/hlink-network-beta/data.json','w'))
