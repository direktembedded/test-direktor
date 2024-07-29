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
# A suite to demonstrate use of Test Template to have all test steps repeatable
#
*** Settings ***
Library          robottestexecutor.proxy.TestExecutorDialogs
Library          testdirektor.example.libraries.PowerMonitor

*** Test Cases ***

VDD Rail
    [Tags]    Power
    [Template]    User Repeat On Fail
    Log To Both
    Verify Vdd          2  4  Low power (VDD) rail could not be detected\n1. Verify Power is on\n2. Ensure PCBA is seated correctly
    Log                 Low Voltage (VDD) rail detected 3.301226

Manual Entries
    [Tags]    User
    [Template]    User Repeat On Fail
    Pause Execution      Execution Paused Intentionally\nPlease Press OK to continue
    Get Value From User  Please enter override PASSWORD\nYou will see password hidden if typing manually  hidden=True
    Get Value From User  Please enter a value\nYou can scan value in\nYou will see value shown if typing manually  0  hidden=False
    Log                  Complete

Firmware Upload
    [Tags]    FW
    Update Firmware      DET003.fw

Reset Verify
    Log                 UART Communications verified after reset

VCC Rail
    [Tags]    Power
    Log                  High Voltage (VCC) rail is as expected 12.10076V

Show Repeat Test Fail
    [Tags]    LED
    [Template]    User Repeat On Fail
    Execute Manual Step  This test demonstrates repeating of tests\nYou can repeat 3 times\nPlease press No to Fail, but Yes to repeat 3 times

Output 1
    Verify Output Sequence  1

Output 2
    Verify Output Sequence  2

Output 3
    Verify Output Sequence  3

Output 4
    Verify Output Sequence  3

Output 5
    Verify Output Sequence  3

Show Repeat Test Pass
    [Tags]    LED
    [Template]    User Repeat On Fail
    Execute Manual Step  This test demonstrates repeating of tests\nPlease press No to Fail first, then Yes to Pass
    Log                  Repeat Test Successful

Input 1
    Verify Input Sequence  1

Input 2
    Verify Input Sequence  2

Input 3
    Verify Input Sequence  3

Input 4
    Verify Input Sequence  4

Input 5
    Verify Input Sequence  5

Remove all Cables
    Log To Suite
    Pause Execution      Please remove all cables from device and move to packing
    Log To Test
    Log                  Package

*** Keywords ***
Verify Output Sequence
    [Arguments]  ${output}
    Log                  Output ${output} PWM sequence matches

Verify Input Sequence
    [Arguments]  ${input}
    Log                  Input ${input} sequence matches

Update Firmware
    [Arguments]  ${fw}
    Log To Test
    FOR                  ${progress}  IN  10%  20%  30%  40%  50%  100%
        Sleep            0.5
        Log              ${progress}
    END

*** Variables ***
${user_repeat_on_fail_count}  3
${user_repeat_on_fail_exit}   True
