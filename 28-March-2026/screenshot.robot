*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/Screenshots
    Open Browser    ${url}   chrome
    Maximize Browser Window
    Sleep    2s
    Capture Page Screenshot  fullpage.png

    Close Browser