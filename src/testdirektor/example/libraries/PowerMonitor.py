#
#  Copyright 2024 Direkt Embedded Pty Ltd
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


from robot.version import get_version

__version__ = get_version()


class PowerMonitor:

    def __init__(self):
        self.vdd = 1

    def verify_vdd(self, min, max, msg):
        self.vdd = self.vdd + 1
        success = float(min) < self.vdd < float(max)
        if not success:
            raise AssertionError(msg)
        return self.vdd
