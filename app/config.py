import json
from app.model.serial_conn import Serializer

def get_config():
	filename = 'config.json'
	with open(filename,'r') as data_file:
		data_json = data_file.read()
		data_json2 = json.loads(data_json)
	return data_json2

serial_conf = get_config()
print serial_conf['config_serial']
test_port = Serializer(port = serial_conf['config_serial']['host'],baudrate=serial_conf['config_serial']['baudrate'],waiting=True)