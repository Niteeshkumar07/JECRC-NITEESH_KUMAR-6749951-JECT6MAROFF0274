*** Settings ***
Library     SeleniumLibrary
Resource    resource/common_resources.robot

*** Test Cases ***
tc1
    Open Application    https://sauce-demo.myshopify.com/
    Sleep    3s
    Close Application

#    robot -d reports -v "BROWSER:edge" <filename>