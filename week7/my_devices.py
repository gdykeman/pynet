"""
pynet-rtr1  (CISCO IOS)     cisco1.twb-tech.com
pynet-rtr2  (CISCO IOS)     cisco2.twb-tech.com
nxos1       (CISCO NX-OS)   nxos1.twb-tech.com
juniper-srx (JUNIPER SRX)   srx1.twb-tech.com
pynet-sw1   (Arista EOS)    arista1.twb-tech.com
pynet-sw2   (Arista EOS)    arista2.twb-tech.com
"""

from getpass import getpass

password = getpass("Enter standard password: ")

pynet_rtr1 = {
    'device_type': 'ios',
    'hostname': 'cisco1.twb-tech.com',
    'username': 'pyclass',
    'password': password,
    'optional_args': {},
}

pynet_rtr2 = {
    'device_type': 'ios',
    'hostname': 'cisco2.twb-tech.com',
    'username': 'pyclass',
    'password': password,
    'optional_args': {},
}

nxos1 = {
    'device_type': 'nxos',
    'hostname': 'nxos1.twb-tech.com',
    'username': 'pyclass',
    'password': password,
    'optional_args': {'port': 8443},
}

pynet_sw1 = {
    'device_type': 'eos',
    'hostname': 'arista1.twb-tech.com',
    'username': 'pyclass',
    'password': password,
    'optional_args': {},
}

pynet_sw2 = {
    'device_type': 'eos',
    'hostname': 'arista2.twb-tech.com',
    'username': 'pyclass',
    'password': password,
    'optional_args': {},
}
juniper_srx = {
    'device_type': 'junos',
    'hostname': 'srx1.twb-tech.com',
    'username': 'pyclass',
    'password': password,
    'optional_args': {},
}

device_list = [
    pynet_rtr1,
    pynet_rtr2,
    nxos1,
    pynet_sw1,
    pynet_sw2,
    juniper_srx,
]
