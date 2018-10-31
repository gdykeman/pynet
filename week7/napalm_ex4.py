#!/usr/bin/env python
from napalm import get_network_driver
from my_devices import device_list

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    new_dict = device_list[4]
    print(new_dict)
#     for remote_device in new_list:
#         device_type = remote_device.pop('device_type')
#         driver = get_network_driver(device_type)
#         device = driver(**remote_device)
#
#         print()
#         print(">>>>Device open")
#
#         device.open()
#
#         print("-" * 50)
#         # device_facts = device.get_facts()
#         device_bgp = device.get_bgp_neighbors()
#         # config = device.get_config()
#
#         # print(device_bgp['global']['peers']['10.220.88.38'])
#         hostname = remote_device['hostname']
#         print("{hostname}:\n".format(hostname=hostname))
#         if '10.220.88.38' in device_bgp['global']['peers']:
#             if device_bgp['global']['peers']['10.220.88.38']['is_up'] == True:
#                 print('Peered with 10.220.88.38 and IS_UP = True')
#             else:
#                 print('Peered with 10.220.88.38 but IS_UP = False')
#         else:
#             print('Not paired with remote bgp peer')
#
#
# if __name__ == "__main__":
#     main()
