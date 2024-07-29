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


"""
This is a dummy library which you can replace with an actual device communications
parser to read values from a device.
Each API/method is provided a default parameter which when set will simply
return that value. In a real implementation this would not be returned, instead
a value would be read from the device.
"""

__version__ = "0.1.0"


class DumyFctParser(object):

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.serial = None

    def get_adc_1(self, default=0):
        return default

    def get_input_1(self, default=0):
        return default

    def set_output_1(self, out: int):
        return out

    def start_fct(self):
        return

    def close_fct(self):
        return
