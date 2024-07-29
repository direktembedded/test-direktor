# Test Direktor &trade;

Test Direktor is a configurable test execution User Interface tool using Robot Framework suite executin with
Test Executor Python UI library for the execution, monitoring and control of python based tests on a device/system.

Multiple device fixtures can be defined for devices/systems each identified by numerous key values
(for example serial number and MAC address) which are configured by the user of this library.

Test Direktor has two modes. A Functional Compliance Test mode as testdirektor.fct and a Diagnostics mode
as testdirektor.fct. The former allows for multiple fixtures which can be run against multiple device suites,
where as the latter is a single fixture with user selectable tests.

## Framework
The UI is a Pyside6/QML based UI and has a listener api which is controlled by a Robot Framework Library for
each fixture defined.

## Configuration
Configuration is achieved using multiple json files. An upper level host configuration defining one
or more fixtures, each of which has a UI configuration and an identifier configuration.

Copyright &copy; 2024 Direkt Embedded Pty Ltd
