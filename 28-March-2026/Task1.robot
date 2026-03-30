*** Settings ***
Documentation  handling dropdowns
Library  SeleniumLibrary

*** Variables ***
${url1}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
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

    @{selected_options}=  Get Selected List Labels    id=colors
    Log To Console    ${selected_options}
    Sleep    2s
    Close Browser

