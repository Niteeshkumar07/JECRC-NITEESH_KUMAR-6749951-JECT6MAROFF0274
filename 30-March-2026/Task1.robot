*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Windows
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Scroll Element Into View    id=PopUp
    
    Click Element    id=PopUp
    Sleep  2s

    @{windows}  Get Window Handles

    Switch Window   NEW
    ${title}  Get Window Titles
    Log To Console    ${title}

    Switch Window   ${windows}[0]

    ${check}  Get Text    class=title
    Sleep   2s
    Page Should Contain    ${check}

    Sleep    2s

    Close Browser





