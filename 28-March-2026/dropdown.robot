*** Settings ***
Documentation  handling dropdowns
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handle dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[text()="Dropdown"]

    Page Should Contain Element    id=dropdown
    Page Should Contain List    id=dropdown

    ${options}=  Get List Items    id=dropdown
    Log To Console    ${options}

    Select From List By Label  id=dropdown    Option 1

    ${select_optiom}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_optiom}
    List Selection Should Be    id=dropdown  Option 1
    Sleep    3s

    Close Browser

handling multiple dropdown
    Open Browser  ${url1}  chrome
    Maximize Browser Window

    Page Should Contain List    id=colors
    Scroll Element Into View    id=colors

    ${options}=  Get List Items    id=colors
    Log To Console    ${options}

    Select From List By Index  id=colors    2
    Select From List By Label  id=colors    Yellow
    Select From List By Value    id=colors  white

    ${selected_options}=  Get Selected List Labels    id=colors
    Log To Console    ${selected_options}
    Sleep    2s
    Close Browser

