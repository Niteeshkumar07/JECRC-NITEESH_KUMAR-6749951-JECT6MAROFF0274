*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows
${url1}  https://www.myntra.com/lehenga-choli?f=Color%3APurple_800080

*** Test Cases ***
Handling Windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/windows/new"]
    Sleep  2s

    @{windows}  Get Window Handles
    @{titles}   Get Window Titles
    Log To Console    ${titles}

    Switch Window   NEW

    Page Should Contain Element    xpath=//h3[text()="New Window"]

    Switch Window   ${windows}[0]
    Go To   ${url1}

    Sleep    2s


    Close Browser





