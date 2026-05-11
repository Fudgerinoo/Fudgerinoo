import json

# 1. Open the JSON file in 'read' mode ('r')
with open('router_data.json', 'r') as file:
    # json.load() converts the JSON text into a Python Dictionary
    network_data = json.load(file)

# 2. Extract top-level data using their Dictionary keys
hostname = network_data['device_role']
mgmt_ip = network_data['management_ip']

print(f"--- Initiating Health Check for {hostname} ({mgmt_ip}) ---")

# 3. The 'interfaces' key contains a List [] of Dictionaries {}.
# We use a 'for' loop to iterate through every interface in that list.
for interface in network_data['interfaces']:
    
    # Extract the specific values for the current interface
    name = interface['name']
    status = interface['status']
    
    # 4. Add some network engineering logic
    if status == "down":
        # If it's down, print an alert and try to grab the VLAN ID
        # We use .get() here because the physical eth0 doesn't have a vlan_id, 
        # and .get() prevents the script from crashing if a key is missing.
        vlan = interface.get('vlan_id', 'N/A')
        print(f"[CRITICAL] Interface {name} (VLAN {vlan}) is DOWN!")
    else:
        print(f"[OK] Interface {name} is operational.")

print("--- Health Check Complete ---")
