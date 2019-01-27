# example of NAPALM comparing running configuration
# with planned changes

import json
from napalm import get_network_driver

bgplist = ['192.168.122.72'
           ]

for ip_address in bgplist:
    driver = get_network_driver('ios')
    iosl2 = driver(ip_address, 'pavel', 'cisco')
    iosl2.open()

    print('\nAccessing:', ip_address)

    iosl2.load_merge_candidate(filename='ACL1.txt')
    diffs = iosl2.compare_config()
    if len(diffs) > 0:
        print("======== Proposed ACL changes ========")
        print(diffs)
        # apply discard_config() when auditing configuration
        iosl2.discard_config()

        # commit_config() can be skipped
        # compare_config() can be used for auditing
        # print("Applying ACL changes")
        # iosl2.commit_config()
    else:
        print("No ACL changes required.")
        iosl2.discard_config()

    iosl2.load_merge_candidate(filename='OSPF1.txt')
    diffs = iosl2.compare_config()
    if len(diffs) > 0:
        print("======== Proposed OSPF changes ========")
        print(diffs)
        # apply discard_config() when auditing configuration
        iosl2.discard_config()

        # commit_config() can be skipped
        # compare_config() can be used for auditing
        # iosl2.commit_config()
    else:
        print("No OSPF changes required.")
        iosl2.discard_config()

    iosl2.close()
