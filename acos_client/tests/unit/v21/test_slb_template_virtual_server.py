# Copyright 2014,  Doug Wiegley,  A10 Networks.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from __future__ import absolute_import
from __future__ import unicode_literals

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from acos_client import client
import responses


HOSTNAME = 'fake_a10'
BASE_URL = "https://{}:443/services/rest/v2.1/?format=json&method=".format(HOSTNAME)
AUTH_URL = "{}authenticate".format(BASE_URL)
CREATE_URL = '{}slb.template.vip.create&session_id={}'.format(BASE_URL, 'foobar')
UPDATE_URL = '{}slb.template.vip.update&session_id={}'.format(BASE_URL, 'foobar')
DELETE_URL = '{}slb.template.vip.delete&session_id={}'.format(BASE_URL, 'foobar')
SEARCH_URL = '{}slb.template.vip.search&session_id={}'.format(BASE_URL, 'foobar')


class TestSLBTemplateCookiePersistence(unittest.TestCase):

    def setUp(self):
        self.client = client.Client(HOSTNAME, '21', 'fake_username', 'fake_password')

    @responses.activate
    def test_slb_template_vip_create_no_parameters(self):
        responses.add(responses.POST, AUTH_URL, json={'session_id': 'foobar'})
        json_response = {
            'response': {'status': 'OK'}
        }
        responses.add(responses.POST, CREATE_URL, json=json_response, status=200)
        params = '{"vip_template": {"name": "test1"}}'

        resp = self.client.slb.template.vip.create('test1')

        self.assertEqual(resp, json_response)
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(responses.calls[1].request.method, responses.POST)
        self.assertEqual(responses.calls[1].request.url, CREATE_URL)
        self.assertEqual(responses.calls[1].request.body, params)

    @responses.activate
    def test_slb_template_vip_create_all_parameters(self):
        responses.add(responses.POST, AUTH_URL, json={'session_id': 'foobar'})
        json_response = {
            'response': {'status': 'OK'}
        }
        responses.add(responses.POST, CREATE_URL, json=json_response, status=200)

        params = ('{"vip_template": {"name": "test1", "conn_limit": {"status": 1, "num": 8000000, "action": 1, '
                  '"logging": 1}, "conn_rate_limit": {"status": true, "num": 1000, "sample_per": 1, "action": 1, '
                  '"logging": true}, "icmp_rate_limit": {"status": true, "normal_rate": 1000, "lockup_status": true, '
                  '"lockup_rate": 10000, "lockup_period": 1000}, "icmpv6_rate_limit": {"status": true, '
                  '"normal_rate": 3, "lockup_status": true, "lockup_rate": 4, "lockup_period": 5}}}'
                  )

        kwargs = {
            "conn_limit": {
                "action": 1,
                "logging": 1,
                "num": 8000000,
                "status": 1
            },
            "conn_rate_limit": {
                "action": 1,
                "logging": 1,
                "num": 1000,
                "sample_per": 1,
                "status": 1
            },
            "icmp_rate_limit": {
                "lockup_period": 1000,
                "lockup_rate": 10000,
                "lockup_status": 1,
                "normal_rate": 1000,
                "status": 1
            },
            "icmpv6_rate_limit": {
                "lockup_period": 5,
                "lockup_rate": 4,
                "lockup_status": 1,
                "normal_rate": 3,
                "status": 1
            },
            "subnet_gratuitous_arp": 0
        }

        resp = self.client.slb.template.vip.create('test1', **kwargs)

        self.assertEqual(resp, json_response)
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(responses.calls[1].request.method, responses.POST)
        self.assertEqual(responses.calls[1].request.url, CREATE_URL)
        self.assertEqual(responses.calls[1].request.body, params)

    @responses.activate
    def test_slb_template_vip_update_no_parameters(self):
        responses.add(responses.POST, AUTH_URL, json={'session_id': 'foobar'})
        json_response = {
            'response': {'status': 'OK'}
        }
        responses.add(responses.POST, UPDATE_URL, json=json_response, status=200)
        params = '{"vip_template": {"name": "test1"}}'

        resp = self.client.slb.template.vip.update('test1')

        self.assertEqual(resp, json_response)
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(responses.calls[1].request.method, responses.POST)
        self.assertEqual(responses.calls[1].request.url, UPDATE_URL)
        self.assertEqual(responses.calls[1].request.body, params)

    @responses.activate
    def test_slb_template_vip_update_all_parameters(self):
        responses.add(responses.POST, AUTH_URL, json={'session_id': 'foobar'})
        json_response = {
            'response': {'status': 'OK'}
        }
        responses.add(responses.POST, UPDATE_URL, json=json_response, status=200)

        params = ('{"vip_template": {"name": "test1", "conn_limit": {"status": 1, "num": 8000000, "action": 1, '
                  '"logging": 1}, "conn_rate_limit": {"status": true, "num": 1000, "sample_per": 1, "action": 1, '
                  '"logging": true}, "icmp_rate_limit": {"status": true, "normal_rate": 1000, "lockup_status": true, '
                  '"lockup_rate": 10000, "lockup_period": 1000}, "icmpv6_rate_limit": {"status": true, '
                  '"normal_rate": 3, "lockup_status": true, "lockup_rate": 4, "lockup_period": 5}}}'
                  )

        kwargs = {
            "conn_limit": {
                "action": 1,
                "logging": 1,
                "num": 8000000,
                "status": 1
            },
            "conn_rate_limit": {
                "action": 1,
                "logging": 1,
                "num": 1000,
                "sample_per": 1,
                "status": 1
            },
            "icmp_rate_limit": {
                "lockup_period": 1000,
                "lockup_rate": 10000,
                "lockup_status": 1,
                "normal_rate": 1000,
                "status": 1
            },
            "icmpv6_rate_limit": {
                "lockup_period": 5,
                "lockup_rate": 4,
                "lockup_status": 1,
                "normal_rate": 3,
                "status": 1
            },
            "subnet_gratuitous_arp": 0
        }

        resp = self.client.slb.template.vip.update('test1', **kwargs)

        self.assertEqual(resp, json_response)
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(responses.calls[1].request.method, responses.POST)
        self.assertEqual(responses.calls[1].request.url, UPDATE_URL)
        self.assertEqual(responses.calls[1].request.body, params)

    @responses.activate
    def test_slb_template_vip_delete(self):
        responses.add(responses.POST, AUTH_URL, json={'session_id': 'foobar'})
        json_response = {
            'response': {'status': 'OK'}
        }
        responses.add(responses.POST, DELETE_URL, json=json_response, status=200)

        resp = self.client.slb.template.vip.delete('test1')

        self.assertEqual(resp, json_response)
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(responses.calls[1].request.method, responses.POST)
        self.assertEqual(responses.calls[1].request.url, DELETE_URL)

    @responses.activate
    def test_slb_template_vip_search(self):
        responses.add(responses.POST, AUTH_URL, json={'session_id': 'foobar'})
        json_response = {
            "vip_template": {
                "conn_limit": {
                    "status": 0
                },
                "conn_rate_limit": {
                    "status": 0
                },
                "name": "sharedVirtualServerTemplate1",
                "subnet_gratuitous_arp": 0
            }
        }
        responses.add(responses.POST, SEARCH_URL, json=json_response, status=200)

        resp = self.client.slb.template.vip.get('test1')

        self.assertEqual(resp, json_response)
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(responses.calls[1].request.method, responses.POST)
        self.assertEqual(responses.calls[1].request.url, SEARCH_URL)
