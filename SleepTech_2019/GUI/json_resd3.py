import json

f = open('test2.json', 'r')
json_dict = json.load(f)
f.close()

temp = json_dict['present']['temperature']
humi = json_dict['present']['humidity']
lumi = json_dict['present']['luminance']

print(temp)
print(humi)
print(lumi)

