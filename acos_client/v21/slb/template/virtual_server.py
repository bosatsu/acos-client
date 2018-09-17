# Copyright 2018, A10 Networks.
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

from acos_client.v21 import base

URL_PREFIX = "slb.template.vip"


class VIP(base.BaseV21):

    def get(self, name, **kwargs):
        return self._post(("{}.search".format(URL_PREFIX)), {'name': name}, **kwargs)

    def _set(self, action, name, **kwargs):

        params = {
            "vip_template": {
                "name": name
            }
        }

        # Enables gratuitous ARP’s for all VIPs in subnet VIPs. Default: 0
        if kwargs.get("subnet_gratuitous_arp", None):
            params["vip_template"]["subnet_gratuitous_arp"] = bool(kwargs["subnet_gratuitous_arp"])

        # Specify maximum number of connections allowed on virtual servers that use this template.
        # "conn_limit" has sub elements. Click on the hyperlink for details.
        if kwargs.get("conn_limit", None):
            params["vip_template"]["conn_limit"] = {}
            # Connection limit status. Default: 0
            if kwargs["conn_limit"].get("status", None):
                params["vip_template"]["conn_limit"]["status"] = int(kwargs["conn_limit"]["status"])
            # Connection limit number. Range: 1 - 8000000, Default: 8000000. Only available when status is set to 1.
            if kwargs["conn_limit"].get("num", None):
                params["vip_template"]["conn_limit"]["num"] = int(kwargs["conn_limit"]["num"])
            # Connection limit action. Drop reset  Range: 0 - 1, Default: 0. Only available when status is set to 1.
            if kwargs["conn_limit"].get("action", None):
                params["vip_template"]["conn_limit"]["action"] = int(kwargs["conn_limit"]["action"])
            # Default: 1. Only available when status is set to 1.
            if kwargs["conn_limit"].get("logging", None):
                params["vip_template"]["conn_limit"]["logging"] = int(kwargs["conn_limit"]["logging"])

        # Limits the rate of new connections ACOS is allowed to send to servers that use this template.
        # "conn_rate_limit" has sub elements. Click on the hyperlink for details.
        if kwargs.get("conn_rate_limit", None):
            params["vip_template"]["conn_rate_limit"] = {}
            # Connection rate limit status. Default: 0
            if kwargs["conn_rate_limit"].get("status", None):
                params["vip_template"]["conn_rate_limit"]["status"] = bool(kwargs["conn_rate_limit"]["status"])
            # Connection rate limit number. Range: 1 - 8000000, Default: 8000000.
            # Only available when status is set to 1.
            if kwargs["conn_rate_limit"].get("num", None):
                params["vip_template"]["conn_rate_limit"]["num"] = int(kwargs["conn_rate_limit"]["num"])
            # Sampling interval. 100 ms 1 second  Range: 0 - 1, Default: 1.
            # Only available when status is set to 1.
            if kwargs["conn_rate_limit"].get("sample_per", None):
                params["vip_template"]["conn_rate_limit"]["sample_per"] = int(kwargs["conn_rate_limit"]["sample_per"])
            # Connection rate limit action.Drop reset  Range: 0 - 1, Default: 0.
            # Only available when status is set to 1.
            if kwargs["conn_rate_limit"].get("action", None):
                params["vip_template"]["conn_rate_limit"]["action"] = int(kwargs["conn_rate_limit"]["action"])
            # Default: 1 (enabled). Only available when status is set to 1.
            if kwargs["conn_rate_limit"].get("logging", None):
                params["vip_template"]["conn_rate_limit"]["logging"] = bool(kwargs["conn_rate_limit"]["logging"])

        # Configures ICMPv4 rate limiting for the virtual server, to protect against denial-of-service (DoS) attacks.
        # "icmp_rate_limit" has sub elements. Click on the hyperlink for details.
        if kwargs.get("icmp_rate_limit", None):
            params["vip_template"]["icmp_rate_limit"] = {}
            # ICMPv4 rate limit status. Default: 0
            if kwargs["icmp_rate_limit"].get("status", None):
                params["vip_template"]["icmp_rate_limit"]["status"] = bool(kwargs["icmp_rate_limit"]["status"])
            # ICMPv4 rate limit normal rate. Range: 1 - 65535, Default: 1000. Only available when status is set to 1.
            if kwargs["icmp_rate_limit"].get("normal_rate", None):
                params["vip_template"]["icmp_rate_limit"]["normal_rate"] = int(
                    kwargs["icmp_rate_limit"]["normal_rate"]
                )
            # ICMPv4 rate limit lockup status. Default: 0 Only available when status is set to 1.
            if kwargs["icmp_rate_limit"].get("lockup_status", None):
                params["vip_template"]["icmp_rate_limit"]["lockup_status"] = bool(
                    kwargs["icmp_rate_limit"]["lockup_status"]
                )
            # ICMPv4 rate limit lockup rate. Range: 1 - 65535, Default: 10000. Only available when status is set to 1.
            if kwargs["icmp_rate_limit"].get("lockup_rate", None):
                params["vip_template"]["icmp_rate_limit"]["lockup_rate"] = int(
                    kwargs["icmp_rate_limit"]["lockup_rate"]
                )
            # ICMPv4 rate limit lockup period. Range: 1 - 16383, Default: 1000. Only available when status is set to 1.
            if kwargs["icmp_rate_limit"].get("lockup_period", None):
                params["vip_template"]["icmp_rate_limit"]["lockup_period"] = int(
                    kwargs["icmp_rate_limit"]["lockup_period"]
                )

        # Configures ICMPv6 rate limiting for the virtual server, to protect against denial-of-service (DoS) attacks.
        # "icmpv6_rate_limit" has sub elements.
        if kwargs.get("icmpv6_rate_limit", None):
            params["vip_template"]["icmpv6_rate_limit"] = {}
            # ICMPv6 rate limit status. Default: 0
            if kwargs["icmpv6_rate_limit"].get("status", None):
                params["vip_template"]["icmpv6_rate_limit"]["status"] = bool(kwargs["icmpv6_rate_limit"]["status"])
            # ICMPv6 rate limit normal rate. Range: 1 - 65535, Default: 1000. Only available when status is set to 1.
            if kwargs["icmpv6_rate_limit"].get("normal_rate", None):
                params["vip_template"]["icmpv6_rate_limit"]["normal_rate"] = int(
                    kwargs["icmpv6_rate_limit"]["normal_rate"]
                )
            # ICMPv6 rate limit lockup status. Default: 0 Only available when status is set to 1.
            if kwargs["icmpv6_rate_limit"].get("lockup_status", None):
                params["vip_template"]["icmpv6_rate_limit"]["lockup_status"] = bool(
                    kwargs["icmpv6_rate_limit"]["lockup_status"]
                )
            # ICMPv6 rate limit lockup rate. Range: 1 - 65535, Default: 10000. Only available when status is set to 1.
            if kwargs["icmpv6_rate_limit"].get("lockup_rate", None):
                params["vip_template"]["icmpv6_rate_limit"]["lockup_rate"] = int(
                    kwargs["icmpv6_rate_limit"]["lockup_rate"]
                )
            # ICMPv6 rate limit lockup period. Range: 1 - 16383, Default: 1000. Only available when status is set to 1.
            if kwargs["icmpv6_rate_limit"].get("lockup_period", None):
                params["vip_template"]["icmpv6_rate_limit"]["lockup_period"] = int(
                    kwargs["icmpv6_rate_limit"]["lockup_period"]
                )

        return self._post(action, params, **kwargs)

    def create(self, name, **kwargs):
        return self._set(("{}.create".format(URL_PREFIX)), name, **kwargs)

    def update(self, name, **kwargs):
        return self._set(("{}.update".format(URL_PREFIX)), name, **kwargs)

    def delete(self, name, **kwargs):
        return self._post(("{}.delete".format(URL_PREFIX)), {'name': name}, **kwargs)
