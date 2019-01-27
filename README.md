# Python Network Programming for Network Engineers (Python 3) - David Bombal course

- netmiko2.py ... simple script running the same tasks on multiple switches:
   "sh ip int br"
   "create int loop 0"
   "create multiple VLANs"
- netmiko3.py ... apply configuration to multiple switches, configuration 
   stored in external plain text file 
- netmiko4.py ... simple script applying the global configuration to "all" switches
   and specific switchport configuration to specific switches; two configuraiton files needed 
- napalm1.py ... basic napalm getters
- napalmconfig2.py ... example of NAPALM comparing running configuration with planned changes 
- napalm_bigevilbeard_example.py ... ref. YouTube video [Managing network configurations with Python automation frameworks NAPALM and Nornir](https://youtu.be/3uIk0WQLHZk)

  list of getters: https://napalm.readthedocs.io/en/latest/support/index.html#getters-support-matrix
