import json

with open('data.json') as json_file:
    data = json.load(json_file)
    for dictionaries in data['nodes']:
        #if 'Biomedical Technology Research Cluster ' in dictionaries['label']:
            #size_ = {'size': 3.0 }
            #dictionaries.update(size_)
        if 'Global Health Disparity Research Cluster ' in dictionaries['label']:
            size_ = {'size': 3.0 }
            color_ = { 'color' : 'rgb(0,38,192)' }
            dictionaries.update(size_)
            dictionaries.update(color_)
        else:
            continue
            #size__ = {'size' : 1.0}
            #dictionaries.update(size__)
json.dump(data,open('data.json','w'))
