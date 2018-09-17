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

URL_PREFIX = "slb.template.tcp"


class TCP(base.BaseV21):

    def get(self, name, **kwargs):
        return self._post(("{}.search".format(URL_PREFIX)), {'name': name}, **kwargs)

    def _set(self, action, name, **kwargs):

        params = {
            "tcp_template": {
                "name": name
            }
        }

        # Specify number of seconds a connection can remain idle before ACOS terminates.
        # Range: 60-2097151, Default: 120.
        if kwargs.get("idle_timeout", None):
            params["udp_template"]["idle_timeout"] = int(kwargs["idle_timeout"])

        # Specify force delete timeout unit. Second 100ms  Range: 0 - 1, Default: 0.
        if kwargs.get("force_del_timeout_unit", None):
            params["udp_template"]["force_del_timeout_unit"] = int(kwargs["force_del_timeout_unit"])

        # Specify maximum number of seconds a session can remain active. Range: 1 - 31, Default: 0.
        if kwargs.get("force_del_timeout", None):
            params["udp_template"]["force_del_timeout"] = int(kwargs["force_del_timeout"])

        # Terminates half-open TCP sessions on the virtual port while allowing active sessions to continue. Default: 0
        if kwargs.get("alive_if_active", None):
            params["udp_template"]["alive_if_active"] = bool(kwargs["alive_if_active"])

        # Set initial TCP window size in SYN ACK packets to clients. Range: 1 - 65535, Default: 0.
        if kwargs.get("init_win_size", None):
            params["udp_template"]["init_win_size"] = int(kwargs["init_win_size"])

        # Enable aging of half-closed TCP sessions. Range: 60 - 15000, Default: 0.
        if kwargs.get("half_close_idle_timeout", None):
            params["udp_template"]["half_close_idle_timeout"] = int(kwargs["half_close_idle_timeout"])

        # Sends a TCP RST to the real server after a session times out.
        if kwargs.get("reset_fwd", None):
            params["udp_template"]["reset_fwd"] = bool(kwargs["reset_fwd"])

        # Sends a TCP RST to the client after a session times out. Default: 0
        if kwargs.get("reset_rec", None):
            params["udp_template"]["reset_rec"] = bool(kwargs["reset_rec"])

        # Increases performance of bidirectional peer sessions by acknowledging receipt of data on behalf of
        # client servers. Default: 0
        if kwargs.get("fast_tcp_acl_on_lan", None):
            params["udp_template"]["fast_tcp_acl_on_lan"] = bool(kwargs["fast_tcp_acl_on_lan"])

        self._post(action, params, **kwargs)

    def create(self, name, **kwargs):
        return self._set(("{}.create".format(URL_PREFIX)), name, **kwargs)

    def update(self, name, **kwargs):
        return self._set(("{}.update".format(URL_PREFIX)), name, **kwargs)

    def delete(self, name, **kwargs):
        return self._post(("{}.delete".format(URL_PREFIX)), {'name': name}, **kwargs)
