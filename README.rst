Test Direktor ™ Application
===========================

*Test Direktor* ™ is a configurable User Interface software for test execution of Robot Framework suites using
*Test Executor* ™ Python UI library for the execution, monitoring and control of python based tests on a test target.

Multiple device fixtures can be defined for the targets, each identified by user configurable key values
(for example serial number and MAC address) for automatic selection of test suites.

*Test Direktor* ™ has two modes. A Functional Compliance Test mode as testdirektor.fct and a Diagnostics mode
as testdirektor.diag. The fct module allows for multiple fixtures which can be run against their corresponding device suites. The diag module is a single fixture with user selectable tests.

Framework
---------
The UI is a Pyside6/QML based UI and has a listener api which is controlled by a Robot Framework Library for
each fixture defined.

Configuration
-------------
Configuration is achieved using multiple json files. An upper level host configuration defining one
or more fixtures, each of which has a section to define the UI layout and another section which configures the target identifiers.

Execution
---------
*Test Direktor* ™ can be executed using any python execution method, including virtual environments
and system installation. We recommend using `pex <https://docs.pex-tool.org/>`_ as it allows you to
distribute identical controlled environments easily to multiple test stations.

Copyright © 2024 Direkt Embedded Pty Ltd
