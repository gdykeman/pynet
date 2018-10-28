#!/usr/bin/env python
from napalm import get_network_driver
from my_devices import device_list

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    for remote_device in device_list:
        device_type = remote_device.pop('device_type')
        # print(device_type)
        driver = get_network_driver(device_type)
        # print(driver)
        device = driver(**remote_device)
        # print(device)

        print()
        print(">>>>Device open")
        device.open()

        print("-" * 50)
        device_facts = device.get_facts()
        # print(device_facts)
        print("{hostname}: Model={model}".format(**device_facts))

    print()

if __name__ == "__main__":
    main()
