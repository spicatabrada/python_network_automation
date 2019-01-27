##############################################################
# Introducation to Napalm
# Author: Stuart Clark <stuaclar@cisco.com>
#
# Demo for Devnet Create 2018 - https://github.com/bigevilbeard/napalm_create
##############################################################


from napalm import get_network_driver
import sys

driver = get_network_driver('ios')
device = driver(hostname='10.10.20.48',
                username='cisco',
                password='cisco_1234!')

device.open()
print('Napalm Is Running........')
device.load_merge_candidate(filename='new_loopbacks.cfg')
diffs = device.compare_config()

if len(diffs) > 0:
    # when only validating configs, always run discard_config()
    print(diffs)

    commit = input("Type COMMIT to commit or hit ENTER to abort: ")
    if commit == 'COMMIT':

        try:
            device.commit_config()

        except Exception as inst:
            print('\nAn error occurred with the commit: ')
            print(type(inst))
            sys.exit(inst)
            print

        else:
            print('Config committed')

    else:
        sys.exit('Script aborted by user')

else:
    print('No changes needed' u"\U0001F37A")
    device.discard_config()

device.close()
