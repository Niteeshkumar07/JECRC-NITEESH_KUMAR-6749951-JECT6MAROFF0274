*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}      chrome

*** Keywords ***
Open Application
    [Documentation]     Opens the application
    [Arguments]     ${url}
    Open Browser    ${url}      ${BROWSER}
    Maximize Browser Window


Close Application
    Close All Browsers

