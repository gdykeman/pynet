#!/usr/bin/env python
from napalm import get_network_driver
from my_devices import device_list

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    new_list = device_list[:2]
    # print(new_list)
    for remote_device in new_list:
        device_type = remote_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**remote_device)

        print()
        print(">>>>Device open")

        device.open()

        print("-" * 50)
        # device_facts = device.get_facts()
        device_lldp = device.get_lldp_neighbors()
        hostname = remote_device['hostname']
        # config = device.get_config()

        print("{hostname}:\n".format(hostname=hostname))
        print(device_lldp)
        print()


if __name__ == "__main__":
    main()
