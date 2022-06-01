import json
import pickle5 as pickle

ghdbiomed= pickle.load(open('SanDiegoHDtokens.pickle','rb')) 

with open('data.json') as json_file:
    data = json.load(json_file)
    for dictionaries in data['nodes']:
        if 'Global Health Disparity Research Cluster ' in dictionaries['label']:
            size_ = {'size': 3.0 }
            dictionaries.update(size_)
        elif 'San Diego Health Disparity Research Cluster ' in dictionaries['label']:
            size_ = {'size': 3.0 }
            color_ = { 'color' : 'rgb(153,255,153)' }
            dictionaries.update(size_)
            dictionaries.update(color_)
        else:
            size__ = {'size' : 1.0}
            dictionaries.update(size__)
        for i in ghdbiomed:
            if i in dictionaries['label']:
                size_ = {'size': 1.0 }
                color_ = { 'color' : 'rgb(153,255,153)' }
                dictionaries.update(size_)
                dictionaries.update(color_)
                
json.dump(data,open('data.json','w'))

