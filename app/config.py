import json

def get_config():
	filename = 'config.json'
	with open(filename,'r') as data_file:
		data_json = data_file.read()
		data_json2 = json.loads(data_json)
	return data_json2


print get_config()