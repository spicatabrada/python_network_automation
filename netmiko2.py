# simple script running the same tasks on multiple switches:
#   "sh ip int br"
#   "create int loop 0"
#   "create multiple VLANs"

from netmiko import ConnectHandler

last_octets = [72, 82, 83]

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.',
    'username': 'pavel',
    'password': 'cisco'
}

for last_octet in last_octets:
    ip_address = '192.168.122.'+str(last_octet)
    iosv_l2["ip"] = ip_address
    print("Processing: ", ip_address)
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_command('show ip int brief')
    print(output)

    config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)

    for n in range(2, 4):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
