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
Test Template    User Repeat On Fail


*** Test Cases ***

Update Firmware
    Verify Vdd           2  4   VDD verify failed, not updating firmware
    Update Firmware      DPC001.fw

Reset Verify
    Sleep               2
    Log                 UARTS Communications verified after reset

VCC Rail
    [Tags]    Power
    Verify Voltage Rail  VCC   12.00023

VDD Rail
    [Tags]    Power
    Verify Voltage Rail  VDD   3.34

Calibrate ADC
    [Tags]    Analog
    Calibrate            Calibrate ADC 1
    Calibrate            Calibrate ADC 2
    Calibrate            Calibrate ADC 3

Output 1
    Verify Output Sequence  1

Output 2
    Verify Output Sequence  2

Output 3
    Verify Output Sequence  3

End Suite
    [Template]          NONE
    ${choice} =         User Choice    Click yes to end suite, no to fail as an example
    Should Be Equal     "${choice}"    "yes"


*** Keywords ***
Calibrate
    [Arguments]  ${data}
    Log                 ${data}
    Log To None
    Sleep               1
    Log To Test

Verify Wireless Signal
    Log                 Wireless signal -77dB

Verify Output Sequence
    [Arguments]  ${output}
    Log                  Output ${output} PWM sequence matches

Verify Voltage Rail
    [Arguments]   ${rail}  ${volts}
    Log                 Low Voltage (${rail}) rail detected ${volts}V

Update Firmware
    [Arguments]  ${fw}
    Log To Both
    FOR                  ${progress}  IN  10%  20%  30%  40%  50%  100%
        Sleep            0.5
        Log              ${progress}
    END

Verify Ethernet
    Log                  Ethernet upload at 0.985GB/s

*** Variables ***
${user_repeat_on_fail_count}  3
