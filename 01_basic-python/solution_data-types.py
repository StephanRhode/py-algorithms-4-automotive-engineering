# The dictionary
a = {'scale': 3.6, 'speed': [0., 15., 22., 30.], 'label': "Scaled speed"}

for i in range(0,len(a['speed'])):
    print(a['label'], a['scale'] * a['speed'][i])
