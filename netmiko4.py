# simple script applying the global configuration to all switches
# and specific switchport configuration to specific switches
# two configuraiton files needed

from netmiko import ConnectHandler


iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.',
    'username': 'pavel',
    'password': 'cisco'
}

# global configuration
last_octets = [82, 83, 84]

with open(r"c:\tmp\iosv_l2_cisco_design.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    print(line)

for last_octet in last_octets:
    ip_address = '192.168.122.'+str(last_octet)
    iosv_l2["ip"] = ip_address
    print("Configuring: ", ip_address)
    net_connect = ConnectHandler(**iosv_l2)

    # send_config_set encapsulates commands with "conf t" and "end"
    output = net_connect.send_config_set(lines)
    print(output)

# core switches configuration
last_octets = [82, 83]

with open(r"c:\tmp\iosv_l2_core.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    print(line)

for last_octet in last_octets:
    ip_address = '192.168.122.'+str(last_octet)
    iosv_l2["ip"] = ip_address
    print("Configuring: ", ip_address)
    net_connect = ConnectHandler(**iosv_l2)

    # send_config_set encapsulates commands with "conf t" and "end"
    output = net_connect.send_config_set(lines)
    print(output)
