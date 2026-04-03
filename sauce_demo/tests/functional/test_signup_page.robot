*** Settings ***
Resource    ../../resource/pages/sign_up_page.robot
Resource    ../../resource/common_resources.robot

Test Setup  Open Application    https://sauce-demo.myshopify.com/
Test Teardown   Close Application


*** Test Cases ***
TC01 Register User
    [Documentation]     check if the user is able to register
    [Tags]  functional

    Sign Up To The Application    Tony    Stark    tonyembark@gmail.com    tony@123

