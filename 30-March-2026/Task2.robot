*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alerts
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionAlert()"]
    Sleep    3s
    Handle Alert

    Sleep    3s
    Close Browser

Confirmation Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionConfirm()"]
    Sleep    3s
    Handle Alert   
    

    ${value}    Get Text    id=demo
    Log To Console    ${value}

    Page Should Contain    ${value}
    Sleep    3s
    Close Browser

Prompt ALert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionPrompt()"]
    Sleep    3s

    Input Text Into Alert    Hello World
    
    ${check}    Get Text    id=demo
    Log To Console    ${check}

    Page Should Contain    ${check}

    Sleep    3s
    Close Browser

