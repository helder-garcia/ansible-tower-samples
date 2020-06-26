#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2020, Helder Garcia <helder.garcia@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: check_connection
short_description: Check reachability of a host/port pair. Think it like the old telnet test.
description:
    - Check if a network port is opened or closed on a remote computer.
    - Automates the popular and manual test using telnet utility.
    - No, it doesn't use telnet. It just tries to open a connection.
version_added: "2.9"
author: "Helder Garcia (@helder-garcia)"
options:
    host:
        description:
            - Target host IP or hostname where to check the TCP/IP reachability.
        required: true
        type: str
    port:
        description:
            - Target port where to check the TCP/IP reachability.
        required: true
        type: int
notes:
    - check_mode is not supported.
    - Do not use '{{ port }}' as a variable name on your playbook, as it is a reserved name. Please, see the example. 
'''

EXAMPLES = '''
- name: check reachability | Try connection on host and port.
  check_connection:
    host: '{{ host }}'
    port: '{{ portnum }}'
'''

RETURN = '''
status:
    description: true if connection was successful, false otherwise
    returned: always
    type: bool
    sample: True
'''

import socket

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type='str', required=True),
            port=dict(type='int', required=True),
        ),
    )

    params = module.params
    result = {}
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rc = clientsocket.connect_ex((params['host'], params['port']))

    if rc == 0:
        result['status'] = True
    else:
        result['status'] = False

    clientsocket.close()

    module.exit_json(**result)


if __name__ == '__main__':
    main()
