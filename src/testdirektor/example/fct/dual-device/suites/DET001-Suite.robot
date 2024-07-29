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
# A suite to demonstrate use of LabJack U3 Input/Output/Analog test device against
# dummy library
# LabJack U3 is controlled via LabJackU3 which is a Robot Framework Library
# Test Setup is
#   LabJack U3
#   Dummy DET003 device
#   LabJack U3         DET003    Label
#     DAC0        ---- adc 1     AI_1
#     AIN0 input  ---- n/a       VDD
#     FIO4 output ---- input 1   DI_1
#     FIO6 input  ---- output 1  DO_1
#

*** Settings ***
Documentation    Functional Compliance Test Suite for DET003 devices
Library          LabJackLibrary.LabJackU3
Library          testdirektor.example.libraries.DummyFctParser
Suite Setup      Open All
Suite Teardown   Close All

*** Test Cases ***

Dummy Test
    Log  something

Verify Vdd
    [Documentation]  Ensure device VDD within bounds ${vdd_min}-${vdd_max}
    ${vdd} =         Get Vdd
    ${bounded}=      Evaluate        ${vdd_min} < ${vdd} < ${vdd_max}
    Should Be True   ${bounded}   message='Vdd ${vdd} not bound by thresholds ${vdd_min}, ${vdd_max}'
    Log              ${vdd}

Test Communications
    ${read}=        Set Output 1  0
    Should Be Equal As Numbers  ${read}  0  message='Failed to communicate with device'
    Log             Communications verified by writing 0 to Output 1

Test ADC 1
    [Documentation]  Verify device ADC accuracy from 0v3 through 3v3
    Verify Adc1 Accuray  0.3  330  0.03
    Verify Adc1 Accuray  1.0  1205  0.03
    Verify Adc1 Accuray  1.5  1827  0.03
    Verify Adc1 Accuray  2.0  2464  0.03
    Verify Adc1 Accuray  2.5  3085  0.03
    Verify Adc1 Accuray  3.0  3718  0.03
    Verify Adc1 Accuray  3.3  4095  0.03

Test Output 1
    Verify Output 1      0
    Verify Output 1      1

Test Input 1
    Verify Input 1       0
    Verify Input 1       1

*** Keywords ***

Get Vdd
    ${vdd}=          Get Analog Input    0
    [return]         ${vdd}

Verify Adc1 Accuray
    [Arguments]      ${write}  ${expected}  ${accuracy}
    [Documentation]  Write value to DAC and read ADC from device and ensure accuracy met
    Set Dac          0  ${write}
    ${adc1} =        Get Adc 1
    ${calculated}=   Evaluate  (${adc1} - ${expected}) / ${expected}
    ${accurate} =    Evaluate  (${calculated} < ${accuracy})
    Should Be True   ${accurate}  message='${write}V. Expected ${expected} read as ${adc1}. Accuracy ${calculated} greater than required ${accuracy}'
    Log              ADC 1 value ${adc1}, error ${calculated}

Verify Output 1
    [Arguments]      ${write}
    [Documentation]  Write value to output and read input from device and ensure equal
    ${output1}=      Set Output 1  ${write}
    ${read}=         Get Di  6
    Should Be Equal As Numbers  ${read}  ${write}  message='Output1 ${read} was read, when expecting ${write}'
    Log              Device output value written ${write} and read ${read}

Verify Input 1
    [Arguments]      ${write}
    [Documentation]  Write value to output and read input from device and ensure equal
    Set Do           4  ${write}
    ${read}=         Get Input 1
    Should Be Equal As Numbers  ${read}  ${write}  message='Input1 ${read} was read, when expecting ${write}'
    Log              Output value written ${write} and device input read ${read}

Delay Toggle Led
    Toggle Led
    Sleep  2

Open U3 And Configure
    [Documentation]  Open only LabJack device found and set all I/O analog, then individually set digitals
    Open Device
    Config Io        fio_analog=0b11111111   # set all to analog before trying config digital
    Config Digital   4  6

Open U3 And Configure Alternate
    [Documentation]  Open only LabJack device found and set all I/O to correct state in one call
    Open Device
    Config Io        fio_analog=0b10101111   # set bit pattern to define 4 and 6 as digital, but less readable

Open All
    Open U3 And Configure
    Start Fct

Close All
    Close Device
    Close Fct


*** Variables ***
${vdd_min}=  3.26
${vdd_max}=  3.34
