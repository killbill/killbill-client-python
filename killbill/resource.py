#
# Copyright 2011-2012 Ning, Inc.
#
# Ning licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

import json

class Resource(object):

    def __init__(self, d):
        self.d = d
        for key, value in d.items():
            setattr(self, key, value)

    def __repr__(self):
        return '%s %s' % (self.__class__, self.d)

    @classmethod
    def fromJson(cls, jsonString):
        return json.loads(jsonString, object_hook=cls.dict_to_object)

    @classmethod
    def dict_to_object(cls, d):
        return cls(d)
