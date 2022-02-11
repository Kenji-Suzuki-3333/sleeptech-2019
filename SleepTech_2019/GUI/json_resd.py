import json

f = open('test.json', 'r')
json_dict = json.load(f)

print('book1の情報：{}'.format(json_dict['book1']))
print('book3のページ数:{}'.format(json_dict['book3']['page']))