import json
import pickle
from collections import Counter
import math
import pandas as pd
import numpy as np
import random
import os 
###
#hlink_tokens = pickle.load(open('/home/jimnoneill/HLINK_top_tokens.pickle','rb'))

group_top_sd_tokens,group_top_hd_tokens = pickle.load(open('/home/jimnoneill/group_top_sd_tokens,group_top_hd_tokens.pickle','rb'))
ghd_tokens = pickle.load(open('/home/jimnoneill/ghd_top_tokens.pickle','rb'))
overlap_tokens = list(set(ghd_tokens).intersection(set(hlink_tokens)))
colors = pickle.load(open('/home/jimnoneill/RGBColors.pickle','rb'))#'/home/jimnoneill/rgb_colors_large.pickle','rb'))
random.shuffle(colors)

pastel_colors = [(156, 216, 238),(248, 241, 212),(255, 253, 245), (246, 207, 185),(226, 252, 218),(202, 241, 233),(211, 238, 255),(224, 217, 215),(180, 206, 179),(228, 216, 185),(255, 250, 182),(250, 222, 203),(180, 222, 144),(236, 157, 182),(219, 255, 190),(198, 156, 207),(231, 185, 247),(194, 238, 214),(137, 224, 216),(225, 222, 157),(136, 254, 209),(249, 230, 161),(219, 189, 228),(145, 129, 154),(222, 224, 243),(243, 154, 210),(129, 167, 200),(255, 173, 170),(148, 239, 191),(161, 207, 219),(160, 181, 219),(216, 153, 187),(187, 130, 138),(212, 255, 143),(194, 179, 246),(221, 206, 133),(255, 179, 211),(255, 153, 202),(233, 128, 251),(251, 197, 144),(151, 169, 156),(236, 235, 194),(217, 128, 179),(154, 201, 157),(225, 166, 137),(156, 232, 227),(215, 208, 226),(214, 251, 190),(240, 253, 217),(137, 255, 222)]
#okenslist = ghd_tokens##[]
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
        size_ = {'size': 2.5 }
        idscolors[idf] = color_change
        data['nodes'][c]['size'] = 2.5
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
        size_ = {'size': 2.5 }
        idscolors[idf] = color_change
        data['nodes'][c]['size'] = 2.5
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
            
            






json.dump(data,open('/home/jimnoneill/projects/NLP_topic_modeling/topicmodel_networks/researchnetworks/hlink_filtered/data.json','w'))
