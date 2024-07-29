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


import argparse
from .. import version


_host_config_help = """Path to file containing host and test fixture configuration.
Configuration file is a json file conforming to a Marshmallow Dataclass as defined in module
testdirektor.control.hostconfig
"""

_test_path_help = """Path to the base folder containing Robot Framework test suites."""

_visibility_help = """Specify how application UI is shown.
Suggested Options: FullScreen, Maximized
Full Options from Qt: https://doc.qt.io/qt-6/qwindow.html#Visibility-enum
"""


_rma_title = 'Test Direktor™ RMA'


def base_argument_parser(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--version', '-v', action='version',
                        version=f'{version.TEST_DIREKTOR_VERSION}')
    parser.add_argument('host_config', help=_host_config_help)
    parser.add_argument('--visibility', help=_visibility_help, default="Maximized")
    return parser


def run():
    from testdirektor.control.engine import Engine

    args = base_argument_parser(_rma_title).parse_args()
    engine = Engine(args.host_config, single_selector=True)
    engine.run(visibility=args.visibility, about_text=f'<b>{_rma_title}</b><p>')
