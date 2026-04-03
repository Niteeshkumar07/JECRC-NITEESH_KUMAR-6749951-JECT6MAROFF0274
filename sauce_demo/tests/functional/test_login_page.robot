*** Settings ***
Resource    ../../resource/pages/login_page.robot
Resource    ../../resource/common_resources.robot

Test Setup  Open Application    https://sauce-demo.myshopify.com/
Test Teardown   Close Application

*** Test Cases ***
TC02 Login User
    Login to the application    tonyembark@gmail.com    tony@123
    
    Sleep    10s