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
short_description: This is a sentence describing the module
description:
    - Longer description of the module.
    - You might include instructions.
version_added: "2.9"
author: "Helder Garcia (@helder-garcia)"
options:
    option_name:
        description:
            - Description of the options goes here.
            - Must be written in sentences.
        required: true or false
        default: a string or the word null
        choices:
          - enable
          - disable
        aliases:
          - repo_name
        version_added: "1.X"
'''

EXAMPLES = '''
# Test we can logon to 'webservers' and execute python with json lib.
# ansible webservers -m ping

# Example from an Ansible Playbook
- ping:

# Induce an exception to see what happens
- ping:
    data: crash
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
        result['status'] = true
    else:
        result['status'] = false

    clientsocket.close()

    module.exit_json(**result)


if __name__ == '__main__':
    main()
