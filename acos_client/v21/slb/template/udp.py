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

URL_PREFIX = "slb.template.udp"


class UDP(base.BaseV21):

    def get(self, name, **kwargs):
        return self._post(("{}.search".format(URL_PREFIX)), {'name': name}, **kwargs)

    def _set(self, action, name, **kwargs):

        params = {
            "udp_template": {
                "name": name
            }
        }

        # Specify number of seconds a connection can reamin idle before ACOS terminates. Range: 60 - 2097151
        # Default: 120.
        if kwargs.get("idle_timeout", None):
            params["udp_template"]["idle_timeout"] = int(kwargs["idle_timeout"])

        # Specify how quickly sessions are terminated. None Immediate Short-Lived  Range: 0 - 2, Default: 0.
        if kwargs.get("aging_type", None):
            params["udp_template"]["aging_type"] = int(kwargs["aging_type"])

        # Short live age. Range: 1 - 31, Default: 0. Only available when aging_type is set to 2.
        if kwargs.get("short_lived", None):
            params["udp_template"]["short_lived"] = int(kwargs["short_lived"])

        # Select another server if server is down. Default: 0
        if kwargs.get("reselect", None):
            params["udp_template"]["reselect"] = bool(kwargs["reselect"])

        # Stateless current connection timeout in seconds. Range: 5 - 120, Default: 0.
        if kwargs.get("stateless_cur_con_timeout", None):
            params["udp_template"]["stateless_cur_con_timeout"] = int(kwargs["stateless_cur_con_timeout"])

        self._post(action, params, **kwargs)

    def create(self, name, **kwargs):
        return self._set(("{}.create".format(URL_PREFIX)), name, **kwargs)

    def update(self, name, **kwargs):
        return self._set(("{}.update".format(URL_PREFIX)), name, **kwargs)

    def delete(self, name, **kwargs):
        return self._post(("{}.delete".format(URL_PREFIX)), {'name': name}, **kwargs)
