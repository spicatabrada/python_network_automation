import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosl2 = driver('192.168.122.72', 'pavel', 'cisco')
iosl2.open()

print('====== get_facts ======')
ios_output = iosl2.get_facts()
print(json.dumps(ios_output, sort_keys=True, indent=2))

print('\n====== get_interfaces ======')
ios_output = iosl2.get_interfaces()
print(json.dumps(ios_output, sort_keys=True, indent=2))

print('\n====== get_interfaces_counters ======')
ios_output = iosl2.get_interfaces_counters()
print(json.dumps(ios_output, sort_keys=True, indent=2))

print('\n====== get_mac_address_table ======')
ios_output = iosl2.get_mac_address_table()
print(json.dumps(ios_output, sort_keys=True, indent=2))

print('\n====== get_arp_table ======')
ios_output = iosl2.get_arp_table()
print(json.dumps(ios_output, sort_keys=True, indent=2))

print('\n====== ping ======')
ios_output = iosl2.ping('8.8.8.8', count=3)
print(json.dumps(ios_output, sort_keys=True, indent=2))

print('\n====== get_bgp_neighbors ======')
ios_output = iosl2.get_bgp_neighbors()
print(json.dumps(ios_output, sort_keys=True, indent=2))

iosl2.close()
