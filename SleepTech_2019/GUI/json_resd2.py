import json

f = open('test2.json', 'r')
json_dict = json.load(f)

temp = json_dict['present']['temperature']
humi = json_dict['present']['humidity']
lumi = json_dict['present']['luminance']

#print('temperature:{}'.format(json_dict['present']['temperature']))
#print('temperature:{}'.format(json_dict['present']['humidity']))
#print('temperature:{}'.format(json_dict['present']['luminance']))

print(temp)
print(humi)
print(lumi)

