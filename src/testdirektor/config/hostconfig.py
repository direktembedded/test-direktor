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

from dataclasses import dataclass, field
from typing import List, Optional

import marshmallow_dataclass


@dataclass
class Host:
    name: str = Optional[str]
    id: str = Optional[str]


@dataclass
class IdentityMonitorConfig:
    module: str = field()
    implementation: str = field()
    arguments: dict


@dataclass
class Fixture:
    title: str = field()
    fixture_id: str = field()
    id_monitor: Optional[IdentityMonitorConfig]


@dataclass
class HostConfig:
    host: Optional[Host]
    id_config: str = field()
    ui_config: str = field()
    db_config: Optional[str]
    base_path: str = field()
    test_path: str = field()
    output_path: str = field()
    title: str = field()
    fixtures: List[Fixture] = field(default_factory=list)
    unique_identifiers: List[str] = field(default_factory=list)


HostConfigSchema = marshmallow_dataclass.class_schema(HostConfig)

example_host_config = """
{
  "host": {
    "name": "optional_name_or_hostname",
    "id": "serial number"
  },
  "fixtures": [
      {
        "title": "station name",
        "fixture_id": "unique identifier"
      }
  ],
  "id_config": "path to identifier configuration",
  "ui_config": "path to ui configuration",
  "db_config": "optional path to database configuration",
  "base_path": "location of path from which ui_config and id_config will take their base if ./ is specified in their path"
  "output_path": "location where output.xml files will be written with suite test results,
  "unique_identifiers": list of keys from id_config which make for a unique identifier for the device e.g. 
                        ["id_key_1", "id_key_2"],
  "title": "application title"
}
"""
