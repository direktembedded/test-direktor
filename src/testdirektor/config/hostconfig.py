#
#  Copyright 2022 (c) Direkt Embedded Pty Ltd
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
