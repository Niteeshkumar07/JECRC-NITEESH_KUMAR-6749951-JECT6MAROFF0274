*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_download}   C:\\Users\\Niteesh Kumar\\Downloads\\file.txt

*** Test Cases ***
File Upload
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/upload"]

    ${path}  Normalize Path   ${CURDIR}/sample.txt

    Choose File    id=file-upload  ${path}
    Sleep    2s
    Click Button    id=file-submit

    Close Browser

Download
    Open Browser    ${url}  chrome
    Click Element    xpath=//a[@href="/download"]
    Sleep    3s

    Click Element    xpath=//a[@href="download/file.txt"]
    Sleep    5s

    Wait Until Created    ${check_download}     timeout=10s

    File Should Exist    ${check_download}
    Log To Console    it downloaded suceesfully

    Close Browser