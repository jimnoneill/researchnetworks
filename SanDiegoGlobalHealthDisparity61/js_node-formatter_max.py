import json
import pickle
import numpy as np
# take nodes and only
ghdbiomed= pickle.load(open('SanDiegoHDtokens.pickle','rb')) 
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
    #elif dictionary['source'] in list(id_label.keys()) or dictionary['target'] in list(id_label.keys()):
        #color_ = dictionary['color'].split(',')
        #color_change = str(int(np.mean([255,int(color_[1])])))
        #color_[1] = color_change
        #color = ",".join(color_)
        #color_change = { 'color' : color }
        #data['edges'][c].update(color_change)
        

                
json.dump(data,open('data.json','w'))
