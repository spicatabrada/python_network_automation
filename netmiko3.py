# simple script running the same tasks on multiple switches
# with configuration stored in external file

from netmiko import ConnectHandler

last_octets = [82, 84]

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.',
    'username': 'pavel',
    'password': 'cisco'
}

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
