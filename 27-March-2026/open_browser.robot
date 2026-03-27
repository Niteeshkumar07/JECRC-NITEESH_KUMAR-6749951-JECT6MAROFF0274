*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary

*** Variables ***
#singular or scalar value
${url}  https://www.cricbuzz.com/
#list variables
@{bikes}  ktm  bmw  pulsar
#dict variables
&{cars}  nissan=gtr  bmw=m4

*** Test Cases ***
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Log    navigating to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Sleep    5s

    Close Browser


Opening Chrome headless Browser
    [Documentation]  Chrome headless browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  ${url}  headlesschrome
    Maximize Browser Window

#    Log    navigating to cricbuzz
    Log To Console    console cricbuzz
    Sleep    5s

    Close Browser

Open cricbuzz in edge
    Open Edge Browser

*** Keywords ***
Open Edge Browser
    [Documentation]  Chrome headless browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  ${url}  edge
    Maximize Browser Window

#    Log    navigating to cricbuzz
    Log To Console    console cricbuzz
    Sleep    5s

    Close Browser



