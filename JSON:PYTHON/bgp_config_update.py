import json

with open('bgp_config.json', 'r') as file:
	bgp_config = json.load(file)

print("The config has successfully loaded")

for neighbor in bgp_config['neighbors']:

	peer_ip = neighbor['peer_ip']
	if(peer_ip == "192.168.122.105"):

		neighbor['admin_status'] = 'up'
		neighbor['hold_timer'] = 30

with open('bgp_deploy.json', 'w') as outfile:
	json.dump(bgp_config, outfile, indent=4) 

print("The changes have been made successfully")
